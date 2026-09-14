import { Link } from "react-router-dom";
import "./ProjectCard.css";

export default function ProjectCard({ project }) {
  return (
    <article className="project-card card">
      {project.image ? (
        <img src={project.image} alt={`${project.title} screenshot`} className="project-card-image" />
      ) : (
        <div className="project-card-image project-card-placeholder" aria-hidden="true">
          <span>{"{ }"}</span>
        </div>
      )}

      <div className="project-card-body">
        <h3>{project.title}</h3>
        <p>{project.summary}</p>

        {project.technologies?.length > 0 && (
          <ul className="project-card-tech">
            {project.technologies.slice(0, 5).map((tech) => (
              <li key={tech.id} className="pill">{tech.name}</li>
            ))}
          </ul>
        )}

        <div className="project-card-links">
          <Link to={`/projects/${project.slug}`} className="btn btn-outline">Case study</Link>
          {project.github_url && (
            <a href={project.github_url} target="_blank" rel="noreferrer" className="project-card-link">
              GitHub ↗
            </a>
          )}
          {project.live_url && (
            <a href={project.live_url} target="_blank" rel="noreferrer" className="project-card-link">
              Live demo ↗
            </a>
          )}
        </div>
      </div>
    </article>
  );
}
