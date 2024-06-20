import { motion } from 'framer-motion'
import { SiPerplexity } from "react-icons/si";
import { AiOutlineOpenAI } from "react-icons/ai";

const svgVariants = {
    initial: {
        rotate: -180,
    },
    animate: {
        rotate: 0,
        transition: { duration: 1 }
    }
}

const OpenaiIcon = () => (
    <motion.div
        variants={svgVariants}
        initial='initial'
        animate='animate'
    >
        <AiOutlineOpenAI size={50} />
    </motion.div>
)

const Perplexity = () => (
    <motion.div>
        <SiPerplexity size={50} />
    </motion.div>

)

const GoogleIcon = ({ width, height }) => (
    <motion.svg
        xmlns="http://www.w3.org/2000/svg"
        width={width}
        height={height}
        viewBox="0 0 256 260"
        variants={svgVariants}
        initial='initial'
        animate='animate'>
        <motion.path fill="#4285f4" d="M255.878 133.451c0-10.734-.871-18.567-2.756-26.69H130.55v48.448h71.947c-1.45 12.04-9.283 30.172-26.69 42.356l-.244 1.622l38.755 30.023l2.685.268c24.659-22.774 38.875-56.282 38.875-96.027" />
        <motion.path fill="#34a853" d="M130.55 261.1c35.248 0 64.839-11.605 86.453-31.622l-41.196-31.913c-11.024 7.688-25.82 13.055-45.257 13.055c-34.523 0-63.824-22.773-74.269-54.25l-1.531.13l-40.298 31.187l-.527 1.465C35.393 231.798 79.49 261.1 130.55 261.1" />
        <motion.path fill="#fbbc05" d="M56.281 156.37c-2.756-8.123-4.351-16.827-4.351-25.82c0-8.994 1.595-17.697 4.206-25.82l-.073-1.73L15.26 71.312l-1.335.635C5.077 89.644 0 109.517 0 130.55s5.077 40.905 13.925 58.602z" />
        <motion.path fill="#eb4335" d="M130.55 50.479c24.514 0 41.05 10.589 50.479 19.438l36.844-35.974C195.245 12.91 165.798 0 130.55 0C79.49 0 35.393 29.301 13.925 71.947l42.211 32.783c10.59-31.477 39.891-54.251 74.414-54.251" />
    </motion.svg>
)

const MetaIcon = ({ width, height }) => (
    <motion.svg
        xmlns="http://www.w3.org/2000/svg"
        width={width}
        height={height}
        viewBox="0 0 256 260"
        variants={svgVariants}
        initial='initial'
        animate='animate'>
        <defs>
            <linearGradient id="logosMetaIcon0" x1="13.878%" x2="89.144%" y1="55.934%" y2="58.694%"><stop offset="0%" stop-color="#0064e1" /><stop offset="40%" stop-color="#0064e1" /><stop offset="83%" stop-color="#0073ee" /><stop offset="100%" stop-color="#0082fb" /></linearGradient>
            <linearGradient id="logosMetaIcon1" x1="54.315%" x2="54.315%" y1="82.782%" y2="39.307%"><stop offset="0%" stop-color="#0082fb" /><stop offset="100%" stop-color="#0064e0" /></linearGradient>
        </defs>
        <path fill="#0081fb" d="M27.651 112.136c0 9.775 2.146 17.28 4.95 21.82c3.677 5.947 9.16 8.466 14.751 8.466c7.211 0 13.808-1.79 26.52-19.372c10.185-14.092 22.186-33.874 30.26-46.275l13.675-21.01c9.499-14.591 20.493-30.811 33.1-41.806C161.196 4.985 172.298 0 183.47 0c18.758 0 36.625 10.87 50.3 31.257C248.735 53.584 256 81.707 256 110.729c0 17.253-3.4 29.93-9.187 39.946c-5.591 9.686-16.488 19.363-34.818 19.363v-27.616c15.695 0 19.612-14.422 19.612-30.927c0-23.52-5.484-49.623-17.564-68.273c-8.574-13.23-19.684-21.313-31.907-21.313c-13.22 0-23.859 9.97-35.815 27.75c-6.356 9.445-12.882 20.956-20.208 33.944l-8.066 14.289c-16.203 28.728-20.307 35.271-28.408 46.07c-14.2 18.91-26.324 26.076-42.287 26.076c-18.935 0-30.91-8.2-38.325-20.556C2.973 139.413 0 126.202 0 111.148z" /><path fill="url(#logosMetaIcon0)" d="M21.802 33.206C34.48 13.666 52.774 0 73.757 0C85.91 0 97.99 3.597 110.605 13.897c13.798 11.261 28.505 29.805 46.853 60.368l6.58 10.967c15.881 26.459 24.917 40.07 30.205 46.49c6.802 8.243 11.565 10.7 17.752 10.7c15.695 0 19.612-14.422 19.612-30.927l24.393-.766c0 17.253-3.4 29.93-9.187 39.946c-5.591 9.686-16.488 19.363-34.818 19.363c-11.395 0-21.49-2.475-32.654-13.007c-8.582-8.083-18.615-22.443-26.334-35.352l-22.96-38.352C118.528 64.08 107.96 49.73 101.845 43.23c-6.578-6.988-15.036-15.428-28.532-15.428c-10.923 0-20.2 7.666-27.963 19.39z" /><path fill="url(#logosMetaIcon1)" d="M73.312 27.802c-10.923 0-20.2 7.666-27.963 19.39c-10.976 16.568-17.698 41.245-17.698 64.944c0 9.775 2.146 17.28 4.95 21.82L9.027 149.482C2.973 139.413 0 126.202 0 111.148C0 83.772 7.514 55.24 21.802 33.206C34.48 13.666 52.774 0 73.757 0z" />
    </motion.svg>
)

const MistralIcon = ({ width, height }) => (
    <motion.svg
        xmlns="http://www.w3.org/2000/svg"
        width={width}
        height={height}
        viewBox="0 0 256 260"
        variants={svgVariants}
        initial='initial'
        animate='animate'>
        <motion.path d="M186.182 0h46.545v46.545h-46.545z" /><motion.path fill="#f7d046" d="M209.455 0H256v46.545h-46.545z" /><motion.path d="M0 0h46.545v46.545H0zm0 46.545h46.545V93.09H0zm0 46.546h46.545v46.545H0zm0 46.545h46.545v46.545H0zm0 46.546h46.545v46.545H0z" /><motion.path fill="#f7d046" d="M23.273 0h46.545v46.545H23.273z" /><motion.path fill="#f2a73b" d="M209.455 46.545H256V93.09h-46.545zm-186.182 0h46.545V93.09H23.273z" /><motion.path d="M139.636 46.545h46.545V93.09h-46.545z" /><motion.path fill="#f2a73b" d="M162.909 46.545h46.545V93.09h-46.545zm-93.091 0h46.545V93.09H69.818z" /><motion.path fill="#ee792f" d="M116.364 93.091h46.545v46.545h-46.545zm46.545 0h46.545v46.545h-46.545zm-93.091 0h46.545v46.545H69.818z" /><motion.path d="M93.091 139.636h46.545v46.545H93.091z" /><motion.path fill="#eb5829" d="M116.364 139.636h46.545v46.545h-46.545z" /><motion.path fill="#ee792f" d="M209.455 93.091H256v46.545h-46.545zm-186.182 0h46.545v46.545H23.273z" /><motion.path d="M186.182 139.636h46.545v46.545h-46.545z" /><motion.path fill="#eb5829" d="M209.455 139.636H256v46.545h-46.545z" /><motion.path d="M186.182 186.182h46.545v46.545h-46.545z" /><motion.path fill="#eb5829" d="M23.273 139.636h46.545v46.545H23.273z" /><motion.path fill="#ea3326" d="M209.455 186.182H256v46.545h-46.545zm-186.182 0h46.545v46.545H23.273z" />
    </motion.svg>
)

const AnthropicIcon = ({ width, height }) => (
    <motion.svg
        xmlns="http://www.w3.org/2000/svg"
        width={width}
        height={height}
        viewBox="0 0 256 176"
        variants={svgVariants}
        initial={{
            rotate: '-180deg',
            scale: 0
        }}
        animate={{ scale: 1, rotate: '0deg' }}
        transition={{ duration: 1 }}
        className='pt-1'>
        <motion.path fill="#1d2e4e" d="m147.487 0l70.081 175.78H256L185.919 0zM66.183 106.221l23.98-61.774l23.98 61.774zM70.07 0L0 175.78h39.18l14.33-36.914h73.308l14.328 36.914h39.179L110.255 0z" />
    </motion.svg>
)

export const llmLogos = {
    'Anthropic': AnthropicIcon,
    'Google': GoogleIcon,
    'Meta': MetaIcon,
    'Mistral AI': MistralIcon,
    'OpenAI': OpenaiIcon,
    'Perplexity AI': Perplexity
}

