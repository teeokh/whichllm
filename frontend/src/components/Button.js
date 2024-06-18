import React from "react";
import ButtonSvg from "../assets/svg/ButtonSvg.js";

const Button = ({ className, href, onClick, children, px, white }) => {
  // Sets tailwind classes for button. If px is not set, it defaults to 'px-7'. Also conditional for colors (white is set in tailwind.config.js)

  // If there is a className passed when actually rendering the button from App.jsx, it will add that, otherwise it will set to an empty string (to not break concatenation)

  // Basically gives some default design for all buttons, then if we want to edit more we can use the className prop in App.jsx
  const classes = `button relative inline-flex items-center justify-center h-11 transition-colors hover:text-blue-600 ${px || "px-7"
    } ${className || ""}`;

  const spanClasses = `relative z-10`;

  const renderButton = () => (
    <button className={classes} onClick={onClick}>
      <span className={spanClasses}>{children}</span>
      {ButtonSvg()}
    </button>
  );

  const renderLink = () => (
    <a href={href} className={classes} onClick={onClick}>
      <span className={spanClasses}>{children}</span>
      {ButtonSvg()}
    </a>
  );

  return href ? renderLink() : renderButton();
};

export default Button;
