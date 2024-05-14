import axios from "axios";
import { useEffect, useState } from "react";

/* eslint-disable react/prop-types */
export default function ProductDetails() {
  const [product, setProduct] = useState(null);
  const token = localStorage.getItem("token");

  // get current id in current pathname
  const id = window.location.pathname.split("/")[2];

  // Add to cart
  const addToCart = async () => {
    // get user id
    const userId = JSON.parse(localStorage.getItem("user")).id;

    await axios.post("/api/cart", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      user_id: userId,
      product_id: id,
      qty: 1,
    });

    // show notification
    document.getElementById("added").classList.remove("hidden");
    setTimeout(() => {
      document.getElementById("added").classList.add("hidden");
    }, 3000);
  };

  useEffect(() => {
    // fetch product from api
    (async () => {
      await axios
        .get(`/api/products/${id}`)
        .then((res) => setProduct(res.data));
    })();
  }, [id]);

  return (
    <>
      <div className="container mx-auto my-16 px-4">
        <div className="flex flex-col items-center justify-center space-x-10 lg:flex-row">
          <div className="mr-8 w-max">
            <img
              src={product?.image_url ?? "/imgs/na.jpg"}
              height={500}
              width={500}
              alt="product"
              className="aspect-square rounded-lg object-cover shadow-lg"
            />
          </div>

          <div className="mt-8 w-full lg:mt-0 lg:w-1/2">
            {/* Product name & description */}
            <h2 className="text-3xl font-bold">{product?.name}</h2>
            <p className="mt-2 text-gray-500">{product?.description}</p>

            {/* sizes radio buttons */}
            <div className="my-5 flex flex-col">
              <p className="mb-3 text-lg font-medium">Sizes</p>
              <div className="flex items-center space-x-3">
                <input id="s" type="radio" name="size" className="radio" />
                <label htmlFor="s">S</label>

                <input id="m" type="radio" name="size" className="radio" />
                <label htmlFor="m">M</label>

                <input id="l" type="radio" name="size" className="radio" />
                <label htmlFor="l">L</label>

                <input id="xl" type="radio" name="size" className="radio" />
                <label htmlFor="xl">XL</label>

                <input id="xxl" type="radio" name="size" className="radio" />
                <label htmlFor="xxl">XXL</label>
              </div>
            </div>

            <p className="mt-10 text-3xl font-semibold">₱{product?.price}</p>
            <button
              className="btn mt-5 w-1/3 px-8 text-white"
              style={{ backgroundColor: "#F68347" }}
              onClick={() => addToCart()}
            >
              Add to cart
            </button>

            {/* Added to cart notification */}
            <div
              id="added"
              className="mt-5 hidden w-max rounded border border-green-400 bg-green-100 px-4 py-3 text-green-700"
            >
              <strong className="font-semibold">Product added to cart</strong>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
