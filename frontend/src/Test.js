import React from 'react'

const Test = () => {
    return (
        <div className='container p-4'>
           <TailwindCSSButton>
                Tailwind Button
           </TailwindCSSButton>
        </div>
    )
}

const TailwindCSSButton = (props) => {
    return ( 
        <button className='bg-blue-500 text-white font-medium px-4 py-2 rounded hover:bg-blue-600'>{props.children}</button>
    );
}

export default Test