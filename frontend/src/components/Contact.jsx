import { useState } from "react";
import { submitContactMessage } from "../api/portfolio";
import "./Contact.css";

const initialForm = { name: "", email: "", subject: "", message: "" };

function validate(form) {
  const errors = {};
  if (form.name.trim().length < 2) errors.name = "Enter your name.";
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) errors.email = "Enter a valid email address.";
  if (form.subject.trim().length < 3) errors.subject = "Subject must be at least 3 characters.";
  if (form.message.trim().length < 10) errors.message = "Message must be at least 10 characters.";
  return errors;
}

export default function Contact({ profile }) {
  const [form, setForm] = useState(initialForm);
  const [errors, setErrors] = useState({});
  const [status, setStatus] = useState("idle"); // idle | submitting | success | error
  const [serverError, setServerError] = useState("");

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const fieldErrors = validate(form);
    setErrors(fieldErrors);
    if (Object.keys(fieldErrors).length > 0) return;

    setStatus("submitting");
    setServerError("");
    try {
      await submitContactMessage(form);
      setStatus("success");
      setForm(initialForm);
    } catch (err) {
      setStatus("error");
      const apiErrors = err?.response?.data;
      if (apiErrors && typeof apiErrors === "object") {
        const messages = Object.values(apiErrors).flat().join(" ");
        setServerError(messages || "Something went wrong. Please try again.");
      } else {
        setServerError("Something went wrong. Please try again.");
      }
    }
  };

  return (
    <section id="contact" className="section contact">
      <div className="container contact-grid">
        <div className="section-head">
          <p className="kicker">Contact</p>
          <h2>Let&rsquo;s work together</h2>
          <p>
            Have a role, project, or freelance opportunity in mind? Send a message and
            I&rsquo;ll get back to you.
          </p>
          {profile?.email && (
            <p className="contact-direct">
              Prefer email? Reach me directly at{" "}
              <a href={`mailto:${profile.email}`}>{profile.email}</a>
            </p>
          )}
        </div>

        <form className="contact-form card" onSubmit={handleSubmit} noValidate>
          <div className="form-row">
            <label htmlFor="name">Name</label>
            <input
              id="name"
              name="name"
              type="text"
              value={form.name}
              onChange={handleChange}
              aria-invalid={Boolean(errors.name)}
              aria-describedby={errors.name ? "name-error" : undefined}
            />
            {errors.name && <p className="form-error" id="name-error">{errors.name}</p>}
          </div>

          <div className="form-row">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              name="email"
              type="email"
              value={form.email}
              onChange={handleChange}
              aria-invalid={Boolean(errors.email)}
              aria-describedby={errors.email ? "email-error" : undefined}
            />
            {errors.email && <p className="form-error" id="email-error">{errors.email}</p>}
          </div>

          <div className="form-row">
            <label htmlFor="subject">Subject</label>
            <input
              id="subject"
              name="subject"
              type="text"
              value={form.subject}
              onChange={handleChange}
              aria-invalid={Boolean(errors.subject)}
              aria-describedby={errors.subject ? "subject-error" : undefined}
            />
            {errors.subject && <p className="form-error" id="subject-error">{errors.subject}</p>}
          </div>

          <div className="form-row">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              name="message"
              rows={5}
              value={form.message}
              onChange={handleChange}
              aria-invalid={Boolean(errors.message)}
              aria-describedby={errors.message ? "message-error" : undefined}
            />
            {errors.message && <p className="form-error" id="message-error">{errors.message}</p>}
          </div>

          <button type="submit" className="btn btn-primary" disabled={status === "submitting"}>
            {status === "submitting" ? "Sending…" : "Send message"}
          </button>

          <div aria-live="polite">
            {status === "success" && (
              <p className="form-status form-status-success">
                Thanks — your message was sent. I&rsquo;ll reply soon.
              </p>
            )}
            {status === "error" && (
              <p className="form-status form-status-error">{serverError}</p>
            )}
          </div>
        </form>
      </div>
    </section>
  );
}
