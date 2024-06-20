import { motion } from 'framer-motion'
import Section from './Section'
import { socials } from '../constants'

const Footer = () => {
    return (
        <Section customPaddings='lg:py-2 px-2' className='!px-0 bottom-0'>
            <div className='container flex sm:justify-between justify-center items-center gap-10 max-sm:flex-col'>
                <p className='caption hidden sm:block'>© {new Date().getFullYear()}. All rights reserved.
                </p>

                <ul className='flex gap-5 flex-wrap'>
                    {socials.map((item) => (
                        <motion.a
                            key={item.id}
                            href={item.url}
                            target='_blank'
                            rel="noreferrer"
                            className='flex items-center justify-center w-10 h-10 rounded-full'
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
