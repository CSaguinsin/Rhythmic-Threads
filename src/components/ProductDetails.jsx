import axios from "axios";
import { useEffect, useState } from "react";

/* eslint-disable react/prop-types */
export default function ProductDetails() {
  const [product, setProduct] = useState(null);

  // get current id in current pathname
  const id = window.location.pathname.split("/")[2];

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
            >
              Add to cart
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
