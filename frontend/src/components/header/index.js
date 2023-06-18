const Header = (props) => {
    return(
        <header className={props.classes}>
            <h1>
                {props.children} <span>{props.highlight}</span>
            </h1>
        </header>
    )
}

export default Header