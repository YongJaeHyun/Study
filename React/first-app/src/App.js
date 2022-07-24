import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Detail from "./routes/Detail.js";
import Home from "./routes/Home.js";

function App() {
  return (
    <Router basename={process.env.PUBLIC_URL}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="movie/:id" element={<Detail />} />
      </Routes>
    </Router>
  );
}

export default App;
