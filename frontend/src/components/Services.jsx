import Loading from "./Loading";
import ErrorState from "./ErrorState";
import EmptyState from "./EmptyState";
import "./Services.css";

export default function Services({ services, loading, error, onRetry }) {
  return (
    <section id="services" className="section services">
      <div className="container">
        <div className="section-head">
          <p className="kicker">Services</p>
          <h2>How I can help</h2>
        </div>

        {loading && <Loading label="Loading services" />}
        {error && <ErrorState message="Couldn't load services from the API." onRetry={onRetry} />}
        {!loading && !error && services?.length === 0 && <EmptyState title="Nothing listed yet" />}

        {!loading && !error && services?.length > 0 && (
          <div className="services-grid">
            {services.map((service) => (
              <div className="service-card card" key={service.id}>
                <h3>{service.title}</h3>
                <p>{service.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
