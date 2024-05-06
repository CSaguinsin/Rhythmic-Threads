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
        <div className="text-center md:text-center sm:text-center pt-10">
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

      <section className="pt-[48px] mx-[78px]">
        <div className="flex flex-row space-x-[886px] px-[70px]">
          <h1 className="text-[32px] font-bold">
            BEST <span style={{ color: "#F68347" }}>SELLERS</span>
          </h1>
          <div className="flex flex-row space-x-2">
            <p className="font-semibold pt-[9px]">SEE ALL</p>
            <img src={seeAll} className="w-[24px] h-[24px] mt-2" />
          </div>
        </div>
        <hr className="h-px my-4 mx-[70px] bg-gray-200 border-0 dark:bg-gray-700" />
        <div className="flex  pt-[27px] space-x-[24px] items-center justify-center px-[70px]">
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

      <section className="pt-[46px] mx-[78px] ">
        <div className="px-[70px]">
          <h1 className="font-bold text-[32px] text-right">
            SHOP BY <span style={{ color: "#F68347" }}>CATEGORY</span>
          </h1>
        </div>
        <div className="flex items-center justify-center mx-[78px] space-x-8">
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-[10rem] h-full">
            <div className="col-span-2 sm:col-span-1 md:col-span-2 bg-gray-50 h-auto w-[536px] md:h-full flex flex-col">
              <a
                href=""
                className="group relative flex flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40 flex-grow"
              >
                <img
                  src={category1}
                  alt=""
                  className="absolute inset-0 h-full w-full object-cover group-hover:scale-105 transition-transform duration-500 ease-in-out"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="z-10 text-2xl font-medium text-white absolute top-0 left-0 p-4 xs:text-xl md:text-3xl">
                  MEN
                </h3>
                <h4 className="text-[16px] font-medium text-white absolute top-10 left-0 p-4 ">
                  SHOP NOW
                </h4>
              </a>
            </div>
            <div className="col-span-2 w-[536px] sm:col-span-1 md:col-span-2 bg-stone-50">
              <a
                href=""
                className="group relative flex flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40 mb-4"
              >
                <img
                  src={category2}
                  alt=""
                  className="absolute inset-0 h-full w-full object-cover group-hover:scale-105 transition-transform duration-500 ease-in-out"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="z-10 text-2xl font-medium text-white absolute top-0 left-0 p-4 xs:text-xl md:text-3xl">
                  WOMEN
                </h3>
                <h4 className="text-[16px] font-medium text-white absolute top-10 left-0 p-4 ">
                  SHOP NOW
                </h4>
              </a>
              <a
                href=""
                className="group relative flex flex-col overflow-hidden rounded-lg px-4 pb-4 pt-40 mb-4"
              >
                <img
                  src={category3}
                  alt=""
                  className="absolute inset-0 h-full w-full  object-cover group-hover:scale-105 transition-transform duration-500 ease-in-out"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-gray-900/25 to-gray-900/5" />
                <h3 className="z-10 text-2xl font-medium text-white absolute top-0 left-0 p-4 xs:text-xl md:text-3xl">
                  KIDS
                </h3>
                <h4 className="text-[16px] font-medium text-white absolute top-10 left-0 p-4 ">
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
          className="hero min-h-screen relative bg-cover bg-center"
          style={{ backgroundImage: `url(${callToAction})` }}
        >
          <div className="hero-content text-center relative z-10">
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
              <div className="flex justify-center pt-5 space-x-3">
                <button
                  className="btn text-white w-[228px] h-[64px]"
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
