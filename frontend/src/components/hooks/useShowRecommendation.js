import { useState } from 'react'

const useShowRecommendation = () => {

    const [showRecommendation, setShowRecommendation] = useState(false)

    const triggerShowRecommendation = () => {
        setShowRecommendation(true)
    }

    const hideRecommendation = () => {
        setShowRecommendation(false)
    }

    return { showRecommendation, triggerShowRecommendation, hideRecommendation }
}

export default useShowRecommendation
