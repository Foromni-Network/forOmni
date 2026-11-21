import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const validator = resolve("scripts/validate-roadmap.mjs");
const valid = {
  project: "foromni",
  canonical_repository: "Foromni-Network/forOmni",
  status_lifecycle: ["proposed","ready","running","review","batch_ready","build_ready","integration_ready","integrated","completed"],
  tasks: [
    { id: "FOR-101", title: "Foundation", phase: 0, status: "ready", dependencies: [], acceptance: ["Document intended outcome"], evidence: [] },
    { id: "FOR-102", title: "Candidate", phase: 1, status: "review", dependencies: ["FOR-101"], acceptance: ["Pass checks"], evidence: [] }
  ]
};
function validate(data) {
  const dir = mkdtempSync(join(tmpdir(), "foromni-roadmap-"));
  try {
    const file = join(dir, "tasks.json");
    writeFileSync(file, JSON.stringify(data));
    return spawnSync(process.execPath, [validator, file], { encoding: "utf8" });
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}
const clone = () => structuredClone(valid);

test("accepts valid baseline", () => assert.equal(validate(clone()).status, 0));
test("rejects duplicate task ids", () => {
  const data = clone(); data.tasks[1].id = "FOR-101";
  assert.notEqual(validate(data).status, 0);
});
test("rejects unknown dependencies", () => {
  const data = clone(); data.tasks[1].dependencies = ["FOR-999"];
  assert.notEqual(validate(data).status, 0);
});
test("rejects dependency cycles", () => {
  const data = clone(); data.tasks[0].dependencies = ["FOR-102"];
  assert.notEqual(validate(data).status, 0);
});
test("rejects unsupported lifecycle states", () => {
  const data = clone(); data.tasks[1].status = "done";
  assert.notEqual(validate(data).status, 0);
});
test("rejects advanced status without evidence", () => {
  const data = clone(); data.tasks[1].status = "build_ready";
  assert.notEqual(validate(data).status, 0);
});
test("rejects advanced status with unpinned evidence", () => {
  const data = clone(); data.tasks[1].status = "build_ready";
  data.tasks[1].evidence = [{ type: "ci", sha: "abc", url: "https://example.com/run/1" }];
  assert.notEqual(validate(data).status, 0);
});
test("accepts exact-SHA linked evidence as structural minimum, not QA approval", () => {
  const data = clone(); data.tasks[1].status = "build_ready";
  data.tasks[1].evidence = [{ type: "ci", sha: "a".repeat(40), url: "https://example.com/run/1", result: "pass" }];
  assert.equal(validate(data).status, 0);
});
