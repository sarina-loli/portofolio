import { Link, useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";
import { getProjectBySlug } from "../api/portfolio";
import Loading from "../components/Loading";
import ErrorState from "../components/ErrorState";
import "./ProjectDetails.css";

export default function ProjectDetails() {
  const { slug } = useParams();

  const {
    data: project,
    error,
    loading,
  } = useFetch(() => getProjectBySlug(slug), [slug]);

  if (loading) {
    return (
      <div className="container project-detail-hero">
        <Loading label="Loading project" />
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="container project-detail-hero">
        <ErrorState
          title="Project not found"
          message="That project doesn't exist or couldn't be loaded."
        />

        <Link
          to="/#projects"
          className="btn btn-outline"
        >
          Back to projects
        </Link>
      </div>
    );
  }

  return (
    <article>

      {/* Project Header */}
      <div className="container project-detail-hero">

        <Link
          to="/#projects"
          className="project-detail-back"
        >
          ← Back to projects
        </Link>

        <div className="project-detail-header">
          <div className="project-detail-title">

            <p className="kicker">
              Case study
            </p>

            <h1>
              {project.title}
            </h1>

            <p>
              {project.summary}
            </p>

          </div>
        </div>

        {/* Technologies */}
        {project.technologies?.length > 0 && (
          <div className="project-detail-tech">

            {project.technologies.map((tech) => (
              <span
                key={tech.id}
                className="pill"
              >
                {tech.name}
              </span>
            ))}

          </div>
        )}

        {/* Main Project Image */}
        {project.image && (
          <img
            src={project.image}
            alt={`${project.title} main screenshot`}
            className="project-detail-image"
          />
        )}

        {/* Additional Project Images */}
        {project.gallery?.length > 0 && (
          <div className="project-gallery">

            <div className="project-gallery-header">
              <p className="kicker">
                Project screenshots
              </p>

              <h2>
                See it in action
              </h2>
            </div>

            <div className="project-gallery-grid">

              {project.gallery.map((item) => (
                <figure
                  key={item.id}
                  className="project-gallery-item"
                >

                  <img
                    src={item.image}
                    alt={
                      item.caption ||
                      `${project.title} screenshot`
                    }
                    className="project-gallery-image"
                  />

                  {item.caption && (
                    <figcaption>
                      {item.caption}
                    </figcaption>
                  )}

                </figure>
              ))}

            </div>

          </div>
        )}

      </div>

      {/* Project Content */}
      <div className="container project-detail-body">

        <div>

          {/* Overview */}
          <div className="project-detail-block">

            <h2>
              Overview
            </h2>

            <p>
              {project.description}
            </p>

          </div>

          {/* Problem */}
          {project.problem && (
            <div className="project-detail-block">

              <h2>
                The problem
              </h2>

              <p>
                {project.problem}
              </p>

            </div>
          )}

          {/* Solution */}
          {project.solution && (
            <div className="project-detail-block">

              <h2>
                The solution
              </h2>

              <p>
                {project.solution}
              </p>

            </div>
          )}

          {/* Architecture */}
          {project.architecture && (
            <div className="project-detail-block">

              <h2>
                Architecture
              </h2>

              <p>
                {project.architecture}
              </p>

            </div>
          )}

          {/* Features */}
          {project.features?.length > 0 && (
            <div className="project-detail-block">

              <h2>
                Key features
              </h2>

              <ul className="project-detail-features">

                {project.features.map((feature) => (
                  <li key={feature}>
                    {feature}
                  </li>
                ))}

              </ul>

            </div>
          )}

          {/* Challenges */}
          {project.challenges && (
            <div className="project-detail-block">

              <h2>
                Challenges
              </h2>

              <p>
                {project.challenges}
              </p>

            </div>
          )}

          {/* Lessons */}
          {project.lessons_learned && (
            <div className="project-detail-block">

              <h2>
                What I learned
              </h2>

              <p>
                {project.lessons_learned}
              </p>

            </div>
          )}

        </div>

        {/* Sidebar */}
        <aside className="project-detail-sidebar card">

          <h3>
            Project links
          </h3>

          {project.github_url && (
            <a
              href={project.github_url}
              target="_blank"
              rel="noreferrer"
              className="btn btn-outline"
            >
              View on GitHub
            </a>
          )}

          {project.live_url && (
            <a
              href={project.live_url}
              target="_blank"
              rel="noreferrer"
              className="btn btn-primary"
            >
              Live demo
            </a>
          )}

          {project.case_study_url && (
            <a
              href={project.case_study_url}
              target="_blank"
              rel="noreferrer"
              className="btn btn-outline"
            >
              Full case study
            </a>
          )}

        </aside>

      </div>

    </article>
  );
}