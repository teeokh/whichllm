export const Rings = () => {
  return (
    <div className="absolute top-1/2 left-1/2 w-[51.375rem] aspect-square border border-blue-500 rounded-full -translate-x-1/2 -translate-y-1/2">
      <div className="absolute top-1/2 left-1/2 w-[36.125rem] aspect-square border border-blue-500 rounded-full -translate-x-1/2 -translate-y-1/2"></div>
      <div className="absolute top-1/2 left-1/2 w-[20.125rem] aspect-square border border-blue-500 rounded-full -translate-x-1/2 -translate-y-1/2"></div>
    </div>
  );
};

export const SideLines = () => {
  return (
    <>
      <div className="absolute top-0 left-5 w-0.25 h-full bg-blue-500"></div>
      <div className="absolute top-0 right-5 w-0.25 h-full bg-blue-200"></div>
    </>
  );
};

export const BackgroundCircles = () => {
  return (
    <>
      <div className="absolute top-[4.4rem] left-16 w-3 h-3 bg-gradient-to-b from-blue-100 to-blue-500 rounded-full"></div>
      <div className="absolute top-[12.6rem] right-16 w-4 h-4 bg-gradient-to-b from-blue-100 to-blue-500 rounded-full"></div>
      <div className="absolute top-[26.8rem] left-16 w-6 h-6 bg-gradient-to-b from-blue-100 to-blue-500 rounded-full"></div>
      <div className="absolute top-[40rem] right-16 w-9 h-9 bg-gradient-to-b from-blue-100 to-blue-500 rounded-full"></div>
    </>
  );
};

export const HamburgerMenu = () => {
  return (
    <div className="absolute inset-0 pointer-events-none lg:hidden">
      <div className="absolute inset-0 opacity-[.03]">
        {/* <img
          className="w-full h-full object-cover"
          width={688}
          height={953}
          alt="Background"
        /> */}
      </div>

      <Rings />

      <SideLines />

      <BackgroundCircles />
    </div>
  );
};
