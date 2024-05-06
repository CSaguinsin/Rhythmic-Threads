import Navbar from "./Navbar";

import heroPic from "/LandingpagePics/heroPic.png";
import bestSeller1 from "/LandingpagePics/bestSeller1.png";
import bestSeller2 from "/LandingpagePics/bestSeller2.png";
import bestSeller3 from "/LandingpagePics/bestSeller3.png";
import seeAll from "/LandingpagePics/seeAll.png";
import category1 from "/LandingpagePics/category1.png";
import category2 from "/LandingpagePics/category2.png";
import category3 from "/LandingpagePics/category3.png";
import callToAction from "../../public/LandingpagePics/callToAction.png";

const Home = () => {
  return (
    <>
      <Navbar />

      {/* Hero section */}
      <section>
        <div className="pt-10 text-center sm:text-center md:text-center">
          <h1 className="text-[48px] font-bold">
            Step into <span style={{ color: "#F68347" }}>Style</span> & Discover{" "}
            <span style={{ color: "#F68347" }}>Fashion</span> <br /> Freedom
            Online with <br />
            <span style={{ color: "#F68347" }}>Every Click</span>
          </h1>
        </div>

        <div className="pt-[48px]">
          <img src={heroPic} className="w-[1366rem]" />
        </div>
      </section>
      {/* End of hero section */}

      <section className="mx-[78px] pt-[48px]">
        <div className="flex flex-row space-x-[886px] px-[70px]">
          <h1 className="text-[32px] font-bold">
            BEST <span style={{ color: "#F68347" }}>SELLERS</span>
          </h1>
          <div className="flex flex-row space-x-2">
            <p className="pt-[9px] font-semibold">SEE ALL</p>
            <img src={seeAll} className="mt-2 h-[24px] w-[24px]" />
          </div>
        </div>
        <hr className="mx-[70px] my-4 h-px border-0 bg-gray-200 dark:bg-gray-700" />
        <div className="flex  items-center justify-center space-x-[24px] px-[70px] pt-[27px]">
          <div className="flex flex-col">
            <img src={bestSeller1} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[220px] pt-[27px]">
              <p className="font-bold">UTILITY JACKET</p>
              <p>₱780</p>
            </div>
          </div>
          <div className="flex flex-col">
            <img src={bestSeller2} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[163px] pt-[27px]">
              <p className="font-bold">SKATER DENIM JACKET</p>
              <p>₱480</p>
            </div>
          </div>
          <div className="flex flex-col">
            <img src={bestSeller3} className="h-[544px] w-[392px]" />
            <div className="flex flex-row space-x-[116px] pt-[27px]">
              <p className="font-bold">OVERSIZED GREY WHITE TEE</p>
              <p>₱900</p>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-[78px] pt-[46px] ">
        <div className="px-[70px]">
          <h1 className="text-right text-[32px] font-bold">
            SHOP BY <span style={{ color: "#F68347" }}>CATEGORY</span>
          </h1>
        </div>
        <div className="mx-[78px] flex items-center justify-center space-x-8">
          <div className="grid h-full grid-cols-1 gap-[10rem] sm:grid-cols-2 md:grid-cols-5">
            <div className="col-span-2 flex h-auto w-[536px] flex-col bg-gray-50 sm:col-span-1 md:col-span-2 md:h-full">
              <a
                href=""
                className="group relative flex flex-grow flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40"
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
                  SHOP NOW
                </h4>
              </a>
            </div>
            <div className="col-span-2 w-[536px] bg-stone-50 sm:col-span-1 md:col-span-2">
              <a
                href=""
                className="group relative mb-4 flex flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40"
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
                  SHOP NOW
                </h4>
              </a>
              <a
                href=""
                className="group relative mb-4 flex flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40"
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
                  SHOP NOW
                </h4>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* <section className='pt-[48px] mx-[78px]'>
       <div className='px-[70px] flex flex-row space-x-[172px]'>
        <h1 className='font-bold text-[32px]'>GET YOURSELF <span style={{ color: '#F68347' }}>SOMETHING</span> TO WEAR IN THIS <span style={{ color: '#F68347' }}>FASHION THREADS</span></h1>
        <p className='text-[16px]'>Find your perfect look with Fashion Threads! Whether it's a casual ensemble or statement piece, we've got you covered. </p>
       </div>

       <div className='flex flex-row pt-[40px]'>

       </div>
    </section> */}

      <section className="pt-[48px]">
        <div
          className="hero relative min-h-screen bg-cover bg-center"
          style={{ backgroundImage: `url(${callToAction})` }}
        >
          <div className="hero-content relative z-10 text-center">
            <div className="">
              <h1 className="text-[80px] font-bold text-white">
                So? What are you{" "}
                <span style={{ color: "#F68347" }}>waiting for?</span>
              </h1>
              <p className="py-6 text-white">
                Don&apos;t hesitate! Dive into Fashion Threads now and pick out
                your next favorite outfit. <br />
                The latest trends are just a click away!.
              </p>
              <div className="flex justify-center space-x-3 pt-5">
                <button
                  className="btn h-[64px] w-[228px] text-white"
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
