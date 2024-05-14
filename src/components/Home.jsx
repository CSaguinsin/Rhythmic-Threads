import Navbar from "./Navbar";

import heroPic from "/LandingpagePics/heroPic.png";
import bestSeller1 from "/LandingpagePics/bestSeller1.png";
import bestSeller2 from "/LandingpagePics/bestSeller2.png";
import bestSeller3 from "/LandingpagePics/bestSeller3.png";
import seeAll from "/LandingpagePics/seeAll.png";
import category1 from "/LandingpagePics/category1.png";
import category2 from "/LandingpagePics/category2.png";
import category3 from "/LandingpagePics/category3.png";
import callToAction from "/LandingpagePics/callToAction.png";

const Home = () => {
  return (
    <>
      <Navbar />

      {/* Hero section */}
      <section className="rounded-2xl py-14 md:mx-36 md:py-20">
        <div className="pb-5 pt-8 text-center sm:text-center md:text-center">
          <h1 className="mx-auto w-2/3 text-7xl font-extrabold leading-tight drop-shadow-lg">
            Step into <span style={{ color: "#F68347" }}>Style</span>,
            <br /> Discover <span style={{ color: "#F68347" }}>Fashion</span>.
          </h1>

          <div className="mx-auto mt-10 flex max-w-max flex-row content-center items-center space-x-2 align-middle">
            <a
              href="/products"
              className="btn h-[64px] w-[228px] rounded-full border-0 text-white shadow-sm"
              style={{ backgroundColor: "#F68347" }}
            >
              Browse Catalog →
            </a>

            <a
              href="/login"
              className="btn btn-ghost h-[64px] w-[228px] border-0 hover:bg-transparent"
            >
              View your orders →
            </a>
          </div>
        </div>
      </section>
      {/* End of hero section */}

      {/* BG Divider */}
      <div className="mb-8 bg-cover">
        <img
          src={heroPic}
          className="aspect-video max-h-[360px] w-full object-cover"
        />
      </div>

      <section className="mx-[78px] pt-[48px]">
        <div className="flex flex-row place-content-between px-[70px]">
          <h1 className="text-3xl font-extrabold">
            BEST <span style={{ color: "#F68347" }}>SELLERS</span>
          </h1>
          <div className="flex flex-row items-center justify-center space-x-2">
            <p className="pt-[9px] font-semibold">SEE ALL</p>
            <img src={seeAll} className="mt-2 h-4 w-4" />
          </div>
        </div>

        <hr className="mx-[70px] my-4 h-px border-0 bg-gray-200 dark:bg-gray-700" />

        <div className="grid grid-cols-1 place-content-center place-items-stretch gap-4 place-self-center px-[70px] pt-[27px] md:place-items-center lg:grid-cols-2 xl:grid-cols-3">
          <div className="flex flex-col">
            <img src={bestSeller1} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[220px] pt-[27px]">
              <p className="text-nowrap font-bold">UTILITY JACKET</p>
              <p>₱780</p>
            </div>
          </div>
          <div className="flex flex-col">
            <img src={bestSeller2} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[163px] pt-[27px]">
              <p className="text-nowrap font-bold">SKATER DENIM JACKET</p>
              <p>₱480</p>
            </div>
          </div>
          <div className="flex flex-col">
            <img src={bestSeller3} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[116px] pt-[27px]">
              <p className="text-nowrap font-bold">OVERSIZED GREY WHITE TEE</p>
              <p>₱900</p>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-[78px] my-20">
        <div className="px-[70px]">
          <h1 className="mb-6 text-right text-3xl font-extrabold">
            SHOP BY <span style={{ color: "#F68347" }}>CATEGORY</span>
          </h1>
        </div>

        <div className="mx-20 flex items-center justify-center space-x-8">
          {/* MENS */}
          <div className="grid h-full min-w-full grid-cols-1 gap-5 place-self-stretch sm:grid-cols-2 md:grid-cols-4">
            <div className="col-span-2 flex h-auto w-full flex-col bg-gray-50 sm:col-span-1 md:col-span-2 md:h-full">
              <a
                href=""
                className="group relative flex flex-grow flex-col overflow-hidden rounded-xl px-4 pb-4 pt-40"
              >
                <img
                  src={category1}
                  alt=""
                  className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 ease-in-out group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="xs:text-xl absolute left-0 top-0 z-10 p-4 text-2xl font-medium text-white md:text-3xl">
                  MEN
                </h3>
                <h4 className="absolute left-0 top-10 p-4 text-[16px] font-medium text-white ">
                  Grab the latest men&apos;s fashion trends.
                </h4>
              </a>
            </div>

            {/* WOMEN AND KIDS ROW */}
            <div className="col-span-2 grid w-full grid-cols-1 grid-rows-2 gap-y-4 place-self-stretch bg-stone-50 sm:col-span-1 md:col-span-2">
              <a
                href=""
                className="group relative flex flex-col overflow-hidden rounded-xl px-4 py-28"
              >
                <img
                  src={category2}
                  alt=""
                  className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 ease-in-out group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="xs:text-xl absolute left-0 top-0 z-10 p-4 text-2xl font-medium text-white md:text-3xl">
                  WOMEN
                </h3>
                <h4 className="absolute left-0 top-10 p-4 text-[16px] font-medium text-white ">
                  Browse through our women&apos;s elegant collection.
                </h4>
              </a>
              <a
                href=""
                className="group relative flex flex-col overflow-hidden rounded-xl px-4 py-28"
              >
                <img
                  src={category3}
                  alt=""
                  className="absolute inset-0 h-full w-full  object-cover transition-transform duration-500 ease-in-out group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="xs:text-xl absolute left-0 top-0 z-10 p-4 text-2xl font-medium text-white md:text-3xl">
                  KIDS
                </h3>
                <h4 className="absolute left-0 top-10 p-4 text-[16px] font-medium text-white ">
                  Find the perfect outfit for your little ones.
                </h4>
              </a>
            </div>
          </div>
        </div>
      </section>

      <section className="my-36">
        <div className="mx-[78px] flex flex-row items-center space-x-[172px] px-[70px]">
          <h1 className="text-[32px] font-extrabold">
            GET YOURSELF <span style={{ color: "#F68347" }}>SOMETHING</span> TO
            WEAR IN THIS{" "}
            <span style={{ color: "#F68347" }}>FASHION THREADS</span>
          </h1>
          <p className="font-medium">
            Find your perfect look with Fashion Threads! Whether it&apos;s a
            casual ensemble or statement piece, we&apos;ve got you covered.{" "}
          </p>
        </div>

        {/* horizontal iamg carousel */}
        <div className="scrollbar-hide ml-[-40px] mt-8 flex h-max flex-row space-x-12 overflow-hidden">
          <img
            src={bestSeller1}
            height={100}
            width={360}
            className="aspect-square max-w-none rounded-xl object-cover"
          />
          <img
            src={bestSeller2}
            height={100}
            width={360}
            className="aspect-square max-w-none rounded-xl object-cover"
          />
          <img
            src={bestSeller3}
            height={100}
            width={360}
            className="aspect-square max-w-none rounded-xl object-cover"
          />
          <img
            src={bestSeller1}
            height={100}
            width={360}
            className="aspect-square max-w-none rounded-xl object-cover"
          />
        </div>
      </section>

      <section className="pt-[48px]">
        <div
          className="hero relative min-h-screen bg-cover bg-center"
          style={{ backgroundImage: `url(${callToAction})` }}
        >
          <div className="hero-content relative z-10 text-center">
            <div className="drop-shadow-lg">
              <h1 className="text-[80px] font-extrabold text-white">
                What are you{" "}
                <span style={{ color: "#F68347" }}>waiting for?</span>
              </h1>
              <p className="py-6 text-white">
                Don&apos;t hesitate! Dive into Fashion Threads now and pick out
                your next favorite outfit. <br />
                The latest trends are just a click away!.
              </p>
              <div className="flex justify-center space-x-3 pt-5">
                <button
                  className="btn h-[64px] w-[228px] rounded-full border-0 text-white shadow-md"
                  style={{ backgroundColor: "#F68347" }}
                >
                  SHOP NOW
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Home;
