import axios from "axios";

const API = "http://127.0.0.1:8000/api/";

export const login = (username, password) =>
  axios.post(API + "auth/login/", { username, password });

export const getTarefas = () => {
  const token = localStorage.getItem("token");
  return axios.get(API + "tarefas/", {
    headers: { Authorization: `Token ${token}` },
  });
};
