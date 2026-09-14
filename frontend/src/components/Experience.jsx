import Loading from "./Loading";
import ErrorState from "./ErrorState";
import EmptyState from "./EmptyState";
import "./Experience.css";

function formatDate(value) {
  if (!value) return "Present";
  const date = new Date(value);
  return date.toLocaleDateString(undefined, { year: "numeric", month: "short" });
}

export default function Experience({ experience, loading, error, onRetry }) {
  return (
    <section id="experience" className="section experience">
      <div className="container">
        <div className="section-head">
          <p className="kicker">Experience</p>
          <h2>Where I&rsquo;ve worked</h2>
        </div>

        {loading && <Loading label="Loading experience" />}
        {error && <ErrorState message="Couldn't load experience from the API." onRetry={onRetry} />}
        {!loading && !error && experience?.length === 0 && (
          <EmptyState title="No experience listed yet" />
        )}

        {!loading && !error && experience?.length > 0 && (
          <ol className="timeline">
            {experience.map((item) => (
              <li className="timeline-item" key={item.id}>
                <div className="timeline-marker" aria-hidden="true" />
                <div className="timeline-content card">
                  <div className="timeline-heading">
                    <h3>{item.position}</h3>
                    <span className="timeline-dates">
                      {formatDate(item.start_date)} — {item.is_current ? "Present" : formatDate(item.end_date)}
                    </span>
                  </div>
                  <p className="timeline-company">
                    {item.company_url ? (
                      <a href={item.company_url} target="_blank" rel="noreferrer">{item.company}</a>
                    ) : (
                      item.company
                    )}
                    {item.location ? <span className="timeline-location"> · {item.location}</span> : null}
                  </p>
                  <p>{item.description}</p>
                  {item.technologies?.length > 0 && (
                    <ul className="timeline-tech">
                      {item.technologies.map((tech) => (
                        <li key={tech} className="pill">{tech}</li>
                      ))}
                    </ul>
                  )}
                </div>
              </li>
            ))}
          </ol>
        )}
      </div>
    </section>
  );
}
