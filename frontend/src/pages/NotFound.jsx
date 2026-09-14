import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <div className="container" style={{ padding: "6rem 0", textAlign: "left" }}>
      <p className="kicker">404</p>
      <h1>This page doesn&rsquo;t exist.</h1>
      <p>The page you're looking for was moved or never existed.</p>
      <Link to="/" className="btn btn-primary">Back home</Link>
    </div>
  );
}
