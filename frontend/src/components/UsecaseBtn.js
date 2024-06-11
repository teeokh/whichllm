import React, { useState, useEffect } from 'react';
import useUsecases from '../components/hooks/useUsecases';
import { icons } from '../assets/icons.js';
import { IconContext } from 'react-icons';
import UsecaseIcon from './UsecaseIcon.js';
import useCategorise from '../components/hooks/useCategorise';

const UsecaseBtn = ({ onSelect }) => {
    const { usecases, error } = useUsecases();
    const [currentIndex, setCurrentIndex] = useState(0);
    const numVisibleUseCases = 3;
    const [selectedUsecase, setSelectedUsecase] = useState(null);
    const [userInput, setUserInput] = useState("");
    const { usecaseId, usecaseName, categoriseError, loading, categoriseText } = useCategorise();
    const [fetchAttempted, setFetchAttempted] = useState(false);

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    const handleCategorise = () => {
        setFetchAttempted(true);
        categoriseText(userInput);
    };

    useEffect(() => {
        if (usecaseId) {
            setSelectedUsecase(usecaseId);
            onSelect(usecaseId); // Call onSelect to update the parent component
        }
        else {
            setSelectedUsecase(null);
        }
    }, [usecaseId, onSelect]);


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
                <h1 className='h1'>Which LLM?</h1>
                <p>Select your desired usecase to find out which AI tool is best for you</p>

                {/* Text box for user input to select category (rather than clicking button) */}
                <input type='text' value={userInput} onChange={handleInputChange} placeholder='What would you like to use AI for?' className='border-2 border-blue-950 rounded-lg p-2 w-80 mt-4 text-center' />
                <button onClick={handleCategorise} className='mt-2'>Submit</button>
                {loading && <p>Loading...</p>}
                {usecaseId && <p> Usecase Category: {usecaseName}</p>}
                {fetchAttempted && !loading && !usecaseId && <p>No clear use case identified, please retry or select from below</p>}

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
                        <div key={usecase.id} className="flex flex-col items-center my-2 lg:my-0 ">

                            {/* Button to indicate which use-case is selected */}
                            <IconContext.Provider value={{ size: 45 }}>
                                <button onClick={() => { setSelectedUsecase(usecase.id); onSelect(usecase.id) }}
                                    className={`lg:mb-4 hover:text-blue-600 ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                >{getUsecaseIcon(usecase.name)}
                                </button>
                            </IconContext.Provider>
                            <div className='flex justify-center w-56'>
                                <button
                                    className={`font-medium hover:text-blue-600 ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                    onClick={() => { setSelectedUsecase(usecase.id); onSelect(usecase.id) }}
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