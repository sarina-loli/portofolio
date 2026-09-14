import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import "./Navbar.css";

const NAV_LINKS = [
  { href: "/#about", label: "About" },
  { href: "/#skills", label: "Skills" },
  { href: "/#projects", label: "Projects" },
  { href: "/#experience", label: "Experience" },
  { href: "/#services", label: "Services" },
  { href: "/#contact", label: "Contact" },
];

export default function Navbar({ profile }) {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);

    window.addEventListener("scroll", onScroll);

    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    // Close the mobile menu whenever the route changes.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setOpen(false);
  }, [location]);

  return (
    <header className={`navbar ${scrolled ? "navbar-scrolled" : ""}`}>
      <div className="container navbar-inner">

        {/* Profile / Logo */}
        <Link to="/" className="navbar-brand">

          {profile?.avatar ? (
            <img
              src={profile.avatar}
              alt={profile?.full_name || "Profile"}
              className="navbar-avatar"
            />
          ) : (
            <span
              className="navbar-brand-mark"
              aria-hidden="true"
            >
              {"</>"}
            </span>
          )}

          <span>
            {profile?.full_name || "Sara Getu"}
          </span>
        </Link>

        {/* Navigation */}
        <nav
          className={`navbar-links ${
            open ? "navbar-links-open" : ""
          }`}
          aria-label="Primary"
          id="navbar-links"
        >
          {NAV_LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              onClick={() => setOpen(false)}
            >
              {link.label}
            </a>
          ))}
        </nav>

        {/* Mobile menu button */}
        <button
          type="button"
          className="navbar-toggle"
          aria-expanded={open}
          aria-controls="navbar-links"
          aria-label={open ? "Close menu" : "Open menu"}
          onClick={() => setOpen((v) => !v)}
        >
          <span />
          <span />
          <span />
        </button>

      </div>
    </header>
  );
}