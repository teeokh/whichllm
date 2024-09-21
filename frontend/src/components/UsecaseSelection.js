import React, { useState, useEffect } from 'react';
// import { useMediaQuery } from 'react-responsive'
import { motion, AnimatePresence } from 'framer-motion'
import useUsecases from './hooks/useUsecases.js';
import { icons } from '../assets/icons.js';
import { IconContext } from 'react-icons';
import useCategorise from './hooks/useCategorise.js';
import Title from './Title.js';

const UsecaseSelection = ({ onSelect, triggerShowRecommendation, hideRecommendation }) => {
    const { usecases, error } = useUsecases();
    const [currentIndex, setCurrentIndex] = useState(0);
    const numVisibleUseCases = 3;
    const [selectedUsecase, setSelectedUsecase] = useState(null);
    const [userInput, setUserInput] = useState("");
    const { usecaseId, usecaseName, loading, categoriseText } = useCategorise();
    const [showUsecaseButtons, setShowUsecaseButtons] = useState(false)
    // const isSmallScreen = useMediaQuery({ minWidth: 640 })
    // const [emptyInput, setEmptyInput] = useState(false)

    const toggleUsecaseButtons = () => {
        setShowUsecaseButtons(!showUsecaseButtons)
    }

    // useEffect(() => {
    //     setShowUsecaseButtons(isSmallScreen);
    // }, [isSmallScreen]);

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    const handleCategorise = () => {
        categoriseText(userInput);
        if (userInput === '') {
            // setEmptyInput(true)
        }
        if (usecaseId) {
            triggerShowRecommendation()
        }
        if (!usecaseId) {
            hideRecommendation()
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
        }
    }, [usecaseId, onSelect, hideRecommendation, triggerShowRecommendation]);

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

            <Title showSubtitle={true} />

            {/* Text box for user input to select category (rather than clicking button) */}
            <form
                onSubmit={(e) => {
                    e.preventDefault()
                    handleCategorise()
                }} className='flex flex-col items-center text-center mt-8'>
                <input
                    type='text'
                    value={userInput}
                    onChange={handleInputChange}
                    placeholder='What would you like to use AI for?'
                    className='border-2 border-blue-950 rounded-xl p-2 w-full text-center' />

                <div className='flex flex-col items-center text-center'>
                    <motion.button
                        whileHover={{ scale: 1.05 }}
                        type='submit'
                        className='button-primary'>Submit
                    </motion.button>
                    {/* <div className='hidden sm:block mt-8 text-slate-500'>Struggling with a use case? Select from a list of use case categories below</div> */}

                    <div className='block mt-8 text-slate-500'>Struggling with a use case? Select from a list of use case categories <button onClick={toggleUsecaseButtons} className='underline' href='#'>here</button></div>
                </div>
            </form>

            <div className='mt-4'>
                {loading && userInput ? <p>Please wait...</p> : null}
                {usecaseId && <p>Use case Category: {usecaseName}</p>}
                {/* {fetchAttempted && !loading && !usecaseId && <p className='mt-8'>No clear use case identified, please retry or choose from the use case list using the link above</p>} */}
            </div>



            {/* Carousel of buttons for use-case selection */}
            <AnimatePresence mode='popLayout'>
                {showUsecaseButtons && (
                    <motion.div
                        initial={{ scale: 0.8, opacity: 0, height: 0 }}
                        animate={{ scale: 1, opacity: 1, height: 'auto' }}
                        exit={{ scale: 0.1, opacity: 0, height: 0 }}
                        transition={{ type: 'spring' }}
                        className="flex items-center mb-[1rem] md:mb-[1.5rem] lg:mb-[2rem]"
                    >
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
                                        <motion.button
                                            whileHover={{ scale: 1.1 }}
                                            onClick={() => {
                                                setSelectedUsecase(usecase.id);
                                                onSelect(usecase.id);
                                                triggerShowRecommendation()
                                            }}
                                            className={`lg:mb-4 pt-4 pb-2 ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                        >
                                            {getUsecaseIcon(usecase.name)}
                                        </motion.button>
                                    </IconContext.Provider>
                                    <div className='flex justify-center w-56'>
                                        <motion.button
                                            whileHover={{ scale: 1.05 }}
                                            className={`font-medium  ${selectedUsecase === usecase.id ? 'text-blue-600' : 'text-blue-950'}`}
                                            onClick={() => {
                                                setSelectedUsecase(usecase.id);
                                                onSelect(usecase.id);
                                                triggerShowRecommendation()
                                            }}
                                        >
                                            {usecase.name}
                                        </motion.button>
                                    </div>

                                </div>
                            ))}
                        </div>

                        {/* Carousel next slide */}
                        <button className="arrow-btn"
                            onClick={nextSlide}
                        // disabled={currentIndex === usecases.length - numVisibleUseCases}
                        >&#8594;</button>
                    </motion.div>
                )}
            </AnimatePresence>

        </div>
    );
}


export default UsecaseSelection;