import React, { useState, useEffect } from 'react';
import useUsecases from './hooks/useUsecases.js';
import { icons } from '../assets/icons.js';
import { IconContext } from 'react-icons';
import UsecaseIcon from './UsecaseIcon.js';
import useCategorise from './hooks/useCategorise.js';
import Button from './Button.js';
import Title from './Title.js';

const UsecaseSelection = ({ onSelect, triggerShowRecommendation, hideRecommendation }) => {
    const { usecases, error } = useUsecases();
    const [currentIndex, setCurrentIndex] = useState(0);
    const numVisibleUseCases = 3;
    const [selectedUsecase, setSelectedUsecase] = useState(null);
    const [userInput, setUserInput] = useState("");
    const { usecaseId, usecaseName, categoriseError, loading, categoriseText } = useCategorise();
    const [fetchAttempted, setFetchAttempted] = useState(false);
    const [usecaseButtonsVisible, setUsecaseButtonsVisible] = useState(false);

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    // Currently not in use
    const handleCategorise = () => {
        setFetchAttempted(true);
        categoriseText(userInput);
        if (usecaseId) {
            triggerShowRecommendation()
            console.log('Rec shown')
        }
        if (!usecaseId) {
            hideRecommendation()
            console.log('Rec hidden')
        }
    };

    useEffect(() => {
        if (usecaseId) {
            setSelectedUsecase(usecaseId);
            onSelect(usecaseId); // Call onSelect to update the parent component
            triggerShowRecommendation()
        }

        if (!usecaseId) {
            setSelectedUsecase(null);
            hideRecommendation()
            console.log('Rec hidden')
        }
    }, [usecaseId, onSelect]);

    const toggleUsecaseButtons = () => {
        setUsecaseButtonsVisible(!usecaseButtonsVisible);
    }

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

            <Title />

            {/* Text box for user input to select category (rather than clicking button) */}
            <div className='flex flex-col items-center text-center mt-8'>
                <input
                    type='text'
                    value={userInput}
                    onChange={handleInputChange}
                    placeholder='What would you like to use AI for?'
                    className='border-2 border-blue-950 rounded-xl p-2 w-96 text-center' />

                <div className='flex flex-col items-center text-center'>
                    <button onClick={handleCategorise} className='button-primary'>Submit</button>
                    <div className='mt-8 text-slate-500'>Struggling with a use case? Select from a list of use case categories below</div>
                </div>

                <div className='mb-8'>
                    {loading && <p className='mt-8'>Please wait...</p>}
                    {usecaseId && <p> Use case Category: {usecaseName}</p>}
                    {fetchAttempted && !loading && !usecaseId && <p className='mt-8'>No clear use case identified, please retry or choose from the use case list using the link above</p>}
                </div>

            </div>

            {/* Carousel of buttons for use-case selection */}


            <div className="flex items-center mb-[1rem] md:mb-[1.5rem] lg:mb-[2rem]">

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
                                <button
                                    onClick={() => {
                                        setSelectedUsecase(usecase.id);
                                        onSelect(usecase.id);
                                        triggerShowRecommendation()
                                    }}
                                    className={`lg:mb-4 hover:text-blue-600 ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                >
                                    {getUsecaseIcon(usecase.name)}
                                </button>
                            </IconContext.Provider>
                            <div className='flex justify-center w-56'>
                                <button
                                    className={`font-medium hover:text-blue-600 ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                    onClick={() => {
                                        setSelectedUsecase(usecase.id);
                                        onSelect(usecase.id);
                                        triggerShowRecommendation()
                                    }}
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


export default UsecaseSelection;