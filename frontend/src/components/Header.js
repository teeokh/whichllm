import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { whichllm } from '../assets/index.js'
import { navigation } from '../constants/index.js'
import Button from './Button.js';
import { HamburgerMenu } from '../components/design/Header.jsx'
import MenuSvg from '../assets/svg/MenuSvg.js'
import { disablePageScroll, enablePageScroll } from "scroll-lock";

const Header = () => {

    const pathName = useLocation();
    const [openNavigation, setOpenNavigation] = useState(true);

    const toggleNavigation = () => {
        if (openNavigation) {
          setOpenNavigation(false);
        } else {
          setOpenNavigation(true);
        }
      };
    
      const handleClick = () => {
        if (!openNavigation) return; // If nav button is clicked and nav is already open, do nothing
    
        enablePageScroll(); // Otherwise allow scrolling to section clicked, and set nav to close
        setOpenNavigation(false);
      };

    return (
        <div className={`fixed top-0 left-0 w-full z-50  border-b border-blue-200 lg:bg-blue-100 lg:backdrop-blur-sm ${openNavigation ? "bg-blue-100" : "bg-blue-100 backdrop-blur-sm"} `}>
            <div className="flex items-center px-5 lg:px-7.5 xl:px-10 max-lg:py-4">

                {/* Logo */}
                <a className='block w-[12rem] xl:mr-8' href='#hero'>
                    <div style={{
                        backgroundImage: `url(${whichllm})`,
                        backgroundPosition: 'center', 
                        backgroundSize: 'cover', 
                        width: '190px',
                        height: '50px',
                    }}></div>
                </a>

                {/* Navigation menu (shows on smaller screens, standard header on larger screens) */}
                <nav className={` ${openNavigation ? "flex" : "hidden"
                    } fixed top-[5rem] left-0 right-0 bottom-0 bg-blue-100 lg:static lg:flex lg:mx-auto lg:bg-transparent `}>
                    <div className="relative z-2 flex flex-col items-center justify-center m-auto lg:flex-row">
                        {navigation.map((item) => (
                            <a
                                key={item.id}
                                href={item.url}
                                onClick={handleClick}
                                className={`block relative text-2xl uppercase text-blue-900 transition-colors hover:text-blue-600 ${item.onlyMobile ? "lg:hidden" : ""
                                    } px-6 py-6 md:py-8 lg:-mr-0.25 lg:text-xs lg:font-semibold ${item.url === pathName.hash
                                        ? "z-2 lg:text-blue-600"
                                        : "lg:text-blue-900"
                                    }`}
                            >
                                {item.title}
                            </a>
                        ))}
                    </div>
                    <HamburgerMenu />
                </nav>

                <a href='#signup' className='button hidden mr-8 text-blue-900 transition-colors hover:text-blue-600 lg:block'>
                    New Account
                </a>
                <Button href="#login" className="hidden lg:flex">
                    Sign In
                </Button>

                <Button className='ml-auto lg:hidden px-3' onClick={toggleNavigation}>
                    <MenuSvg openNavigation={openNavigation}/>
                </Button>
            </div>
        </div>
    );
}

export default Header;