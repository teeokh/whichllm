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

        
        <div className='flex flex-col items-center flex-wrap'>
            <div className='flex flex-col items-center mb-10 text-center'>
                <h1 className='font-bold text-4xl'>Which LLM?</h1>
                <p>Select your desired usecase to find out which AI tool is best for you</p>
            </div>
            
            <div className="flex items-center">
            

                {/* Carousel previous slide  */}
                <button className="arrow-btn"
                    onClick={prevSlide}
                // disabled={currentIndex === 0}
                >&#8592;
                </button>

                <div className="flex flex-col lg:flex-row overflow-hidden">
                    {visibleUsecases.map((usecase) => (
                        <div key={usecase.id} className="flex flex-col items-center my-2 lg:my-0 lg:-space-x-3">

                            {/* Button to indicate which use-case is selected */}
                            <IconContext.Provider value={{ size: 50 }}>
                                <button onClick={() => onSelect(usecase.id)} className='lg:mb-4'>
                                    {getUsecaseIcon(usecase.name)}
                                </button>
                            </IconContext.Provider>
                            <div className='flex justify-center w-56'>
                            <button
                                className="text-black font-medium"
                                onClick={() => onSelect(usecase.id)}
                            >
                                {usecase.name}
                            </button>
                            </div>
                            
                        </div>
                    ))}
                </div>

                {/* Carousel next slide */}
                <button className="arrow-btn"
                    onClick={nextSlide}
                // disabled={currentIndex === usecases.length - numVisibleUseCases}
                >&#8594;</button>
            </div>
        </div>
    );
}

export default UsecaseBtn;
