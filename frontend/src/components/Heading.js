import React from 'react'

const Heading = ({ className, title }) => {
    return (
        <div
            className={`${className} max-w-full mx-auto mb-8 lg:mb-12`}>
            {title && <h2 className='h2'>{title}</h2>}
        </div>
    )
}

export default Heading
