import { readFileSync } from "node:fs";

const file = process.argv[2] ?? "roadmap/tasks.json";
const data = JSON.parse(readFileSync(file, "utf8"));
const validStatuses = ["proposed","ready","running","review","batch_ready","build_ready","integration_ready","integrated","completed"];
const requireEvidence = new Set(["batch_ready","build_ready","integration_ready","integrated","completed"]);
const errors = [];
if (data.project !== "foromni" || data.canonical_repository !== "Foromni-Network/forOmni") errors.push("Incorrect project/repository identity");
if (JSON.stringify(data.status_lifecycle) !== JSON.stringify(validStatuses)) errors.push("Unexpected lifecycle");
if (!Array.isArray(data.tasks)) errors.push("tasks must be an array");
const tasks = Array.isArray(data.tasks) ? data.tasks : [];
const ids = new Set();
for (const [index, t] of tasks.entries()) {
  const p = `tasks[${index}]`;
  if (typeof t.id !== "string" || !/^FOR-[0-9]{3,}$/.test(t.id)) errors.push(`${p}: invalid id`);
  if (ids.has(t.id)) errors.push(`${p}: duplicate id ${t.id}`);
  ids.add(t.id);
  if (typeof t.title !== "string" || !t.title.trim()) errors.push(`${p}: missing title`);
  if (!Number.isInteger(t.phase) || t.phase < 0 || t.phase > 4) errors.push(`${p}: invalid roadmap phase`);
  if (!validStatuses.includes(t.status)) errors.push(`${p}: invalid status`);
  if (!Array.isArray(t.dependencies) || !Array.isArray(t.acceptance) || !Array.isArray(t.evidence)) errors.push(`${p}: dependencies, acceptance and evidence must be arrays`);
  if (Array.isArray(t.acceptance) && t.acceptance.length === 0) errors.push(`${p}: acceptance criteria required`);
  if (requireEvidence.has(t.status) && (!Array.isArray(t.evidence) || t.evidence.length === 0)) errors.push(`${p}: ${t.status} requires linked evidence`);
  if (["build_ready","integration_ready","integrated","completed"].includes(t.status) && !(t.evidence ?? []).some(e => e && typeof e.sha === "string" && /^[0-9a-f]{40}$/.test(e.sha) && typeof e.url === "string" && /^https:\/\//.test(e.url))) errors.push(`${p}: ${t.status} requires exact commit SHA and evidence URL`);
}
for (const t of tasks) {
  if (!Array.isArray(t.dependencies)) continue;
  for (const d of t.dependencies) {
    if (!ids.has(d)) errors.push(`${t.id}: missing dependency ${d}`);
    if (d === t.id) errors.push(`${t.id}: self dependency`);
  }
}
const byId = new Map(tasks.map(t => [t.id,t]));
const visited = new Set(), active = new Set();
function checkCycles(id) {
  if (active.has(id)) { errors.push(`dependency cycle involving ${id}`); return; }
  if (visited.has(id)) return;
  active.add(id);
  for (const d of byId.get(id)?.dependencies ?? []) if (byId.has(d)) checkCycles(d);
  active.delete(id); visited.add(id);
}
for (const id of ids) checkCycles(id);
if (errors.length) { console.error(errors.join("\n")); process.exit(1); }
console.log(`Validated ${tasks.length} Foromni roadmap tasks; no advanced statuses accepted without evidence.`);
