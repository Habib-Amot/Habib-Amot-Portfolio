export default function NavItem({icon, text, href, active }) {
    return (
        <li className={`nav-item flex items-center justify-center w-[121.73px] h-10.25 rounded-[41px] ${active && "active"}`}>
            <a href={href} className="flex items-center justify-center gap-2 text-gray-800 text-sm font-semibold h-full w-full p-1">
                {icon}
                <p className="text-sm font-semibold">{text}</p>
            </a>
        </li>
    );
}