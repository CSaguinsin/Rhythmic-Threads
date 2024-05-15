import { useEffect, useState } from "react";
import axios from "axios";

import localStorage from "../utils/localStorage";

export default function Cart() {
  const [data, setData] = useState([]);
  const [total, setTotal] = useState(0);

  const token = localStorage.getItem("token");

  useEffect(() => {
    axios
      .get("/api/cart", {
        headers: {
          Authorization: `Bearer ${token.replace(/['"]+/g, "")}`,
        },
      })
      .then((res) => {
        setData(res.data);
      })
      .then(() => {
        let total = 0;
        data.forEach((item) => {
          total += item.product.price * item.qty;
        });
        setTotal(total);
      })
      .catch((error) => console.error("Error:", error.response));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  return (
    <>
      {/* Shopping cart */}
      <div className="container mx-auto w-full px-4 py-12 md:w-3/4 md:px-6">
        <div className="grid gap-8">
          <div className="grid gap-6">
            <div className="flex items-center justify-between">
              <h1 className="text-2xl font-bold">Shopping Cart</h1>
            </div>

            {data?.map((item) => (
              <div key={item.id} className="grid gap-6">
                <div className="grid max-w-full items-center justify-between gap-4 border-b pb-4 sm:grid-cols-2">
                  <div className="flex w-full items-center space-x-5">
                    <img
                      alt={null}
                      className="aspect-square rounded-lg object-cover"
                      height={100}
                      src={item?.image_url ?? "/imgs/na.jpg"}
                      width={100}
                    />
                    <div className="grid gap-1">
                      <h3 className="text-xl font-semibold">
                        {item?.product?.name}
                      </h3>
                      <p className="line-clamp-2 h-11 overflow-hidden text-ellipsis text-sm text-gray-500 dark:text-gray-400">
                        {item?.product?.description}
                      </p>
                    </div>
                  </div>

                  <div className="flex w-full items-center justify-end gap-4 text-right">
                    <div className="flex items-center gap-1">
                      <p>
                        Size: <span className="uppercase">{item?.size}</span>
                      </p>
                      <p> Qty. {item?.qty}</p>
                    </div>

                    <span className="font-semibold">
                      ₱{(item?.product?.price * item?.qty).toFixed(2)}
                      <span className="ml-1 font-normal">
                        ({Number(item?.product?.price).toFixed(2)})
                      </span>
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Total */}
          <div className="grid gap-4 pt-6">
            <div className="flex items-center justify-between">
              <span className="text-lg font-semibold">Total</span>
              <span className="text-2xl font-bold">₱{total}</span>
            </div>

            {/* Buttons */}
            <div className="mt-5 flex justify-end gap-4 align-middle">
              <a href="/landingpage" className="ghost btn px-7">
                Continue Shopping
              </a>
              <button className="btn bg-[#F68347] px-7 text-white">
                Proceed to Checkout
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
