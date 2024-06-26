import React from 'react'

const Title = ({ showSubtitle }) => {

    return (
        <div className='flex flex-col items-center text-center'>
            <h1 className='h1'>Which LLM?</h1>
            {showSubtitle && <p>Enter your desired use case to find out which AI tool is best for you</p>}
        </div>
    )
}

export default Title
