import React from 'react'

const Section = ({
    className, customPaddings, customPosition, children
}) => {
    return (
        <>
            <div className={`${className || ''} ${customPosition || 'relative'} ${customPaddings || 'py-5 lg:py-10 xl:py-12 px-7'} `}>                {children}

                {/* <div className='hidden absolute top-0 left-5 w-[1px] h-full bg-blue-200 pointer-events-none md:block lg:left-7.5 xl:left-8'></div>
                <div className='hidden absolute top-0 right-5 w-[1px] h-full bg-blue-200 pointer-events-none md:block lg:right-7.5 xl:right-8'></div>
                <div className='hidden absolute bottom-0 w-full h-[1px] bg-blue-200 pointer-events-none md:block'></div> */}
            </div>
        </>
    )
}

export default Section
