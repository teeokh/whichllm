import { useEffect } from "react";

const Modal = ({ show, hide, message, header }) => {

    // Scroll lock whilst modal is open
    useEffect(() => {
        if (show) {
            document.body.style.overflow = 'hidden';
        }
        return () => {
            document.body.style.overflow = 'unset';
        };
    }, [show]);

    return (
        <>

            {show ? (
                <>
                    <div
                        className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
                    >
                        <div className="relative w-auto my-6 mx-auto max-w-sm">

                            {/*content*/}
                            <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none text-center">

                                {/*header*/}
                                <div className="flex items-start justify-center p-5 border-b border-solid border-blueGray-200 rounded-t text-center text-3xl">
                                    {header}
                                </div>

                                {/*body*/}
                                <div className="relative p-6 flex-auto">
                                    <p className="my-4 text-blueGray-500 text-lg leading-relaxed">
                                        {message}
                                    </p>
                                </div>

                                {/*footer*/}
                                <div className="flex items-center justify-start p-6 border-t border-solid border-blueGray-200 rounded-b">
                                    <button
                                        className="text-blue-950 background-transparent font-bold px-4 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150 border border-blue-950 rounded-lg"
                                        type="button"
                                        onClick={hide}
                                    >
                                        Okay
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
                </>
            ) : null}
        </>
    );
}

export default Modal;