import "./Skills.css";

const CATEGORY_ORDER = ["frontend", "backend", "database", "security", "tools", "other"];
const CATEGORY_LABELS = {
  frontend: "Frontend",
  backend: "Backend",
  database: "Database",
  security: "Authentication & Security",
  tools: "Tools & Deployment",
  other: "Other",
};

export default function Skills({ skills = [] }) {
  const grouped = CATEGORY_ORDER.map((key) => ({
    key,
    label: CATEGORY_LABELS[key],
    items: skills.filter((s) => s.category === key),
  })).filter((group) => group.items.length > 0);

  return (
    <section id="skills" className="section skills">
      <div className="container">
        <div className="section-head">
          <p className="kicker">Skills</p>
          <h2>Tools I reach for</h2>
          <p>Grouped by where they show up in the stack, from interface to database.</p>
        </div>

        <div className="skills-grid">
          {grouped.map((group) => (
            <div className="skills-card card" key={group.key}>
              <h3>{group.label}</h3>
              <ul className="skills-list">
                {group.items.map((skill) => (
                  <li key={skill.id} className="skill-row">
                    <span className="skill-name">{skill.name}</span>
                    <span className="skill-bar" aria-hidden="true">
                      <span
                        className="skill-bar-fill"
                        style={{ width: `${skill.proficiency}%` }}
                      />
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
