import { useOutletContext } from "react-router-dom";
import Hero from "../components/Hero";
import About from "../components/About";
import Skills from "../components/Skills";
import Projects from "../components/Projects";
import Experience from "../components/Experience";
import Education from "../components/Education";
import Services from "../components/Services";
import GithubSection from "../components/GithubSection";
import Contact from "../components/Contact";
import useFetch from "../hooks/useFetch";
import {
  getSkills,
  getProjects,
  getExperience,
  getEducation,
  getServices,
} from "../api/portfolio";

export default function Home() {
  const { profile } = useOutletContext();

  const skillsFetch = useFetch(getSkills, []);
  const projectsFetch = useFetch(() => getProjects({ ordering: "order" }), []);
  const experienceFetch = useFetch(getExperience, []);
  const educationFetch = useFetch(getEducation, []);
  const servicesFetch = useFetch(getServices, []);

  const projectResults = projectsFetch.data?.results ?? projectsFetch.data ?? [];

  return (
    <>
      <Hero profile={profile} />
      <About profile={profile} />
      <Skills skills={skillsFetch.data || []} />
      <Projects
        projects={projectResults}
        loading={projectsFetch.loading}
        error={projectsFetch.error}
      />
      <Experience
        experience={experienceFetch.data || []}
        loading={experienceFetch.loading}
        error={experienceFetch.error}
      />
      <Education
        education={educationFetch.data || []}
        loading={educationFetch.loading}
        error={educationFetch.error}
      />
      <Services
        services={servicesFetch.data || []}
        loading={servicesFetch.loading}
        error={servicesFetch.error}
      />
      <GithubSection
        profile={profile}
        featuredProjects={projectResults.filter((p) => p.featured)}
      />
      <Contact profile={profile} />
    </>
  );
}
