import useShowRecommendation from './hooks/useShowRecommendation.js';


const { showRecommendation, triggerShowRecommendation, hideRecommendation } = useShowRecommendation();


const SearchAgain = () => {
    return (
        <div className='mt-10'>
            <button className='button-primary' onClick={hideRec}>Search Again?</button>
        </div>
    )
}

export default SearchAgain
