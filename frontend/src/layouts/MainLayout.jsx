import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import useFetch from "../hooks/useFetch";
import { getProfile } from "../api/portfolio";

export default function MainLayout() {
  const { data: profile } = useFetch(getProfile, []);

  return (
    <>
      <a href="#main-content" className="skip-link">Skip to content</a>
      <Navbar profile={profile} />
      <main id="main-content">
        <Outlet context={{ profile }} />
      </main>
      <Footer profile={profile} />
    </>
  );
}
