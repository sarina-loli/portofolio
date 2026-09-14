import api from "./client";

export const getProfile = () => api.get("/profile/").then((res) => res.data);

export const getSkills = (category) =>
  api.get("/skills/", { params: category ? { category } : {} }).then((res) => res.data);

export const getProjects = (params = {}) =>
  api.get("/projects/", { params }).then((res) => res.data);

export const getProjectBySlug = (slug) =>
  api.get(`/projects/${slug}/`).then((res) => res.data);

export const getExperience = () => api.get("/experience/").then((res) => res.data);

export const getEducation = () => api.get("/education/").then((res) => res.data);

export const getServices = () => api.get("/services/").then((res) => res.data);

export const submitContactMessage = (payload) =>
  api.post("/contact/", payload).then((res) => res.data);
