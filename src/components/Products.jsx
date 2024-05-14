/* eslint-disable react/prop-types */
import { useState, useEffect } from "react";
import axios from "axios";

import AuthNavbar from "../authcomponents/AuthNavbar";
import { ProductCard } from "./ProductCard";
import { useSearchParams } from "react-router-dom";

export default function Products({ user }) {
  const [data, setData] = useState([]);
  const [params, setParams] = useSearchParams();

  useEffect(() => {
    axios
      .get("/api/products", {
        params: {
          ratings: params.get("ratings"),
          category: params.get("category"),
          collection: params.get("collection"),
          size: params.get("size"),
        },
      })
      .then((res) => {
        setData(res.data);
      });
  }, [params]);

  return (
    <>
      <AuthNavbar user={user} />

      <div className="flex h-full space-x-6 space-y-8 p-8 md:mx-[78px] md:flex">
        <div className="flex w-full">
          {/* Filter Sidebar */}
          <div className="relative w-1/4 p-4">
            <form className="sticky left-0 top-24 z-0 space-y-6 overflow-hidden px-1">
              <div>
                <h3 className="text-lg font-semibold">Product Categories</h3>
                <div className="mt-2 space-y-2">
                  <div className="flex items-center space-x-2">
                    <input
                      id="men"
                      name="category"
                      type="radio"
                      value="men"
                      onChange={() => {
                        params.set("category", "men");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="men"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      Men
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="women"
                      name="category"
                      type="radio"
                      value="women"
                      onChange={() => {
                        params.set("category", "women");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="women"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      Women
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="kids"
                      value="kids"
                      name="category"
                      type="radio"
                      onChange={() => {
                        params.set("category", "kids");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="kids"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      Kids
                    </label>
                  </div>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold">Filter by Product</h3>
                <div className="mt-2 space-y-2">
                  <div className="flex items-center space-x-2">
                    <input
                      id="shorts"
                      name="collection"
                      type="radio"
                      value="shorts"
                      onChange={() => {
                        params.set("collection", "shorts");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="shorts"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      Shorts
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="jackets"
                      name="collection"
                      type="radio"
                      value="jackets"
                      onChange={() => {
                        params.set("collection", "jackets");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="jackets"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      Jackets
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="tshirts"
                      type="radio"
                      name="collection"
                      value="tshirts"
                      onChange={() => {
                        params.set("collection", "t-shirts");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="tshirts"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      T-Shirts
                    </label>
                  </div>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold">Filter by Size</h3>
                <div className="mt-2 space-y-2">
                  <div className="flex items-center space-x-2">
                    <input
                      id="s"
                      type="radio"
                      name="size"
                      value="s"
                      onChange={() => {
                        params.set("size", "s");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="s"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      S
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="m"
                      name="size"
                      type="radio"
                      value="m"
                      onChange={() => {
                        params.set("size", "m");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="m"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      M
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="l"
                      type="radio"
                      name="size"
                      value="l"
                      onChange={() => {
                        params.set("size", "l");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="l"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      L
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="xl"
                      type="radio"
                      name="size"
                      value="xl"
                      onChange={() => {
                        params.set("size", "xl");
                        setParams(params);
                      }}
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                    />
                    <label
                      htmlFor="xl"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      XL
                    </label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      id="xxl"
                      type="radio"
                      value="xxl"
                      name="size"
                      className="radio-warning radio h-4 w-4 rounded-md border-gray-300 bg-gray-100 text-blue-600 focus:ring-2 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-blue-600"
                      onChange={() => {
                        params.set("size", "xxl");
                        setParams(params);
                      }}
                    />
                    <label
                      htmlFor="xxl"
                      className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                      XXL
                    </label>
                  </div>

                  <div className="flex w-full items-center pt-4">
                    <button
                      type="reset"
                      className="btn px-5"
                      onClick={() => setParams()}
                    >
                      Reset
                    </button>
                  </div>
                </div>
              </div>
            </form>
          </div>

          {/* Grid content */}
          <div className="grid-rows-auto grid h-max w-full grid-cols-1 content-stretch items-stretch gap-8 p-4 md:grid-cols-2 lg:grid-cols-3">
            {data?.map((product) => (
              <ProductCard key={product?.id} product={product} />
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
