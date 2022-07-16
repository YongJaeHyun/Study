import { useState, useEffect } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [userMoney, setUserMoney] = useState(0);
  const [coinMoney, setCoinMoney] = useState(Infinity);
  const [resultMoney, setResultMoney] = useState(0);
  const [coinSymbol, setCoinSymbol] = useState("");
  const [coins, setCoins] = useState([]);

  const onChangeInput = (e) => {
    setUserMoney(e.target.value);
  };

  const onChangeSelect = (e) => {
    const price = coins[e.target.selectedIndex - 1].quotes.USD.price;
    const symbol = coins[e.target.selectedIndex - 1].symbol;
    setCoinMoney(parseFloat(price));
    setCoinSymbol(symbol);
  };

  useEffect(() => {
    setResultMoney(userMoney / coinMoney);
  }, [userMoney, coinMoney]);

  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
  }, []);
  return (
    <div>
      <h1>The Coins! {loading ? "" : `(${coins.length})`}</h1>
      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <form>
          <input type="number" value={userMoney} onChange={onChangeInput} />
          <hr />
          <select onChange={onChangeSelect}>
            <option>Select Coin!</option>
            {coins.map((coin) => (
              <option key={coin.id}>
                {coin.name} ({coin.symbol}): ${coin.quotes.USD.price} USD
              </option>
            ))}
          </select>
        </form>
      )}
      <h3>
        your money: ${userMoney} -{`>`} {resultMoney}
        {coinSymbol}
      </h3>
    </div>
  );
}

export default App;
