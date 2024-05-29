import React from 'react'
import Button from './Button'

const Section = ({
    className, customPaddings, children
}) => {
    return (
        <>
            <div className={`relative ${customPaddings || `py-5 lg:py-10 xl:py-15 px-2 ${className || ''}`}`}>
                {children}
                <div className='hidden absolute top-0 left-5 w-[1px] h-full bg-blue-200 pointer-events-none md:block lg:left-7.5 xl:left-10'></div>
                <div className='hidden absolute top-0 right-5 w-[1px] h-full bg-blue-200 pointer-events-none md:block lg:right-7.5 xl:right-10'></div>
            </div>
        </>
    )
}

export default Section
