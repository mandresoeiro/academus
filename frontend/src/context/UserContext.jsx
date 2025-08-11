import { createContext, useContext, useState, useEffect } from "react";
import { getToken } from "../services/authService";

const UserContext = createContext();

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = getToken();
    if (token) {
      const savedUser = localStorage.getItem("user");
      if (savedUser) setUser(savedUser);
    }
  }, []);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

export const useUser = () => useContext(UserContext);
