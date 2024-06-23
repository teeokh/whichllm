import { motion } from 'framer-motion'
import Section from './Section'
import { socials } from '../constants'

const Footer = () => {
    return (
        <Section customPaddings='py-2 px-0 md:px-8' className='bottom-0 mb-5 sm:mb-0'>
            <div className='container flex sm:justify-between justify-center items-center max-sm:flex-col'>
                <p className='caption hidden sm:block'>© {new Date().getFullYear()}. All rights reserved.
                </p>

                <ul className='flex gap-7 sm:gap-5 flex-wrap'>
                    {socials.map((item) => (
                        <motion.a
                            key={item.id}
                            href={item.url}
                            target='_blank'
                            rel="noreferrer"
                            className='flex items-center justify-center md:w-10 md:h-10 rounded-full w-5 h-5'
                            whileHover={{ scale: 1.25 }}>
                            <img
                                src={item.iconUrl}
                                width={16}
                                height={16}
                                alt={item.title}
                            />
                        </motion.a>
                    ))}
                </ul>
            </div>

        </Section>
    )
}

export default Footer
