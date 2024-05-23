import React, { useState } from 'react';
import useUsecases from '../components/hooks/useUsecases';
import { icons } from '../assets/icons.js';
import { IconContext } from 'react-icons';
import UsecaseIcon from './UsecaseIcon.js';

const UsecaseBtn = ({ onSelect }) => {
    const { usecases, error } = useUsecases();
    const [currentIndex, setCurrentIndex] = useState(0);
    const numVisibleUseCases = 3;

    if (error) {
        return <p>{error}</p>;
    }

    if (usecases.length === 0) {
        return <p></p>;
    }

    const getUsecaseIcon = (usecaseName) => {
        const IconComponent = icons[usecaseName];
        return IconComponent ? <IconComponent /> : null;
    }

    // For carousel effect
    const prevSlide = () => {
        setCurrentIndex((prevIndex) =>
            prevIndex === 0 ? usecases.length - numVisibleUseCases : prevIndex - 1
        );
    };


    const nextSlide = () => {
        setCurrentIndex((prevIndex) =>
            prevIndex === usecases.length - numVisibleUseCases ? 0 : prevIndex + 1
        );
    };

    const visibleUsecases = usecases.slice(
        currentIndex,
        currentIndex + numVisibleUseCases
    );

    return (

        
        <div className='flex flex-col items-center'>
            <div className='flex flex-col items-center mb-10'>
                <h1 className='font-bold text-3xl'>Which LLM?</h1>
                <p>Select your desired usecase to find out which AI tool is best for you</p>
            </div>
            
            <div className="flex items-center">
            

                {/* Carousel previous slide  */}
                <button className="px-2 py-1 mr-2 text-white bg-black hover:text-black hover:bg-white hover:border-solid hover:border-black border rounded-full size-2xl"
                    onClick={prevSlide}
                // disabled={currentIndex === 0}
                >&#8592;
                </button>

                <div className="flex overflow-hidden">
                    {visibleUsecases.map((usecase) => (
                        <div key={usecase.id} className="flex flex-col items-center px-2">

                            {/* Button to indicate which use-case is selected */}
                            <IconContext.Provider value={{ size: 50 }}>
                                <button onClick={() => onSelect(usecase.id)} className='m-4'>
                                    {getUsecaseIcon(usecase.name)}
                                </button>
                            </IconContext.Provider>
                            <div className='flex justify-center w-56 p-2'>
                            <button
                                className="text-black"
                                onClick={() => onSelect(usecase.id)}
                            >
                                {usecase.name}
                            </button>
                            </div>
                            
                        </div>
                    ))}
                </div>

                {/* Carousel next slide */}
                <button className="px-2 py-1 mr-2 text-white bg-black hover:text-black hover:bg-white hover:border-solid hover:border-black border rounded-full size-2xl"
                    onClick={nextSlide}
                // disabled={currentIndex === usecases.length - numVisibleUseCases}
                >&#8594;</button>
            </div>
        </div>
    );
}

export default UsecaseBtn;
