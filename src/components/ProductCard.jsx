/* eslint-disable react/prop-types */
export const ProductCard = ({ product }) => (
  <d className="w-full max-w-sm overflow-hidden rounded-xl bg-white shadow-lg">
    <a
      href={"/products/" + product.id}
      className="flex aspect-[4/3] items-center justify-center bg-gray-100"
    >
      <img
        alt={null}
        className="aspect-square h-full w-full border-none object-cover"
        height={300}
        src={product.imageUrl ?? "/imgs/na.jpg"}
        width={400}
      />
    </a>

    <div className="space-y-4 p-6">
      <a href={"/products/" + product.id} className="text-xl font-semibold">
        {product.name}
      </a>
      <p className="text-lg font-semibold">₱{product.price}</p>

      <p className="line-clamp-3 w-full overflow-hidden text-ellipsis text-pretty text-sm text-gray-500">
        {product.description}
      </p>

      <a
        href={"/products/" + product.id}
        className="btn w-full px-8 text-white"
        style={{ backgroundColor: "#F68347" }}
      >
        Buy Now
      </a>
    </div>
  </d>
);
