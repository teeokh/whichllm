import React, { useState } from 'react';
import useUsecases from '../components/hooks/useUsecases';

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
            <div className="flex items-center p-4">

                {/* Carousel previous slide  */}
                <button className="px-2 py-1 mr-2 text-white bg-blue-500 hover:bg-teal-300 rounded-full"
                    onClick={prevSlide}
                    // disabled={currentIndex === 0}
                >&#8592;
                </button>

                <div className="flex overflow-hidden">
                    {visibleUsecases.map((usecase) => (
                        <div key={usecase.id} className="px-2">
                            {/* Button to indicate which use-case is selected */}
                            <button
                                className="text-white bg-blue-500 hover:to-blue-500 font-small rounded-md hover:bg-teal-300 w-56 p-2"
                                onClick={() => onSelect(usecase.id)}
                            >
                                {usecase.name}
                            </button>
                        </div>
                    ))}
                </div>

                {/* Carousel next slide */}
                <button className="px-2 py-1 ml-2 text-white bg-blue-500 hover:bg-teal-300 rounded-full"
                    onClick={nextSlide}
                    // disabled={currentIndex === usecases.length - numVisibleUseCases}
                >&#8594;</button>
            </div>

            {/* Small buttons to indicate which usecase has been selected (remove last 2 so you can continuously scroll through) */}
            <div className="flex space-x-2">
                {usecases.slice(0, -2).map((_, index) => (
                    <button
                        key={index}
                        className={`p-2 rounded-full hover:bg-teal-300 ${index === currentIndex ? 'bg-teal-300' : 'bg-blue-500'}`}
                        onClick={() => setCurrentIndex(index)} />
                ))}
            </div>
        </div>
    );
};

export default UsecaseBtn;
