import axios from "axios";
import { useEffect } from "react";
import { useParams } from "react-router-dom";

function Detail() {
  const { id } = useParams();
  const getMovie = async () => {
    const json = await (
      await axios.get(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).data;
    console.log(json);
  };

  useEffect(() => {
    getMovie();
  });
  return <h1>Detail</h1>;
}
export default Detail;
