import ProjectCard from "./ProjectCard";
import Loading from "./Loading";
import ErrorState from "./ErrorState";
import EmptyState from "./EmptyState";
import "./Projects.css";

export default function Projects({ projects, loading, error, onRetry }) {
  return (
    <section id="projects" className="section projects">
      <div className="container">
        <div className="section-head">
          <p className="kicker">Featured projects</p>
          <h2>Things I&rsquo;ve built</h2>
          <p>Full-stack applications with a Django REST API on the back end and React on the front.</p>
        </div>

        {loading && <Loading label="Loading projects" />}
        {error && <ErrorState message="Couldn't load projects from the API." onRetry={onRetry} />}
        {!loading && !error && projects?.length === 0 && (
          <EmptyState
            title="No projects published yet"
            message="Check back soon — projects are managed from the Django admin."
          />
        )}
        {!loading && !error && projects?.length > 0 && (
          <div className="projects-grid">
            {projects.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
