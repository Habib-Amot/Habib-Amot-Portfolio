import logo from "../../assets/TestLogo.svg"
import home from "../../assets/icons/home.svg"
import chat from "../../assets/icons/chat.svg"
import group from "../../assets/icons/group.svg"
import calendar from "../../assets/icons/calendar.svg"
import settings from "../../assets/icons/settings.svg"
import more_vert from "../../assets/icons/more_vert.svg"
import credit_card from "../../assets/icons/credit_card.svg"
import profile_image from "../../assets/images/senior-woman-doctor.png"

import NavItem from "../atomic/Nav/NavItem";

export default function NavBar(){
    let navItems = [
        {icon: <img src={home} alt="Home" />, text: "Overview", href: "/", active:false},
        {icon: <img src={group} alt="Patients" />, text: "Patients", href: "/patients", active:true},
        {icon: <img src={calendar} alt="Schedule" />, text: "Schedule", href: "/schedule", active:false},
        {icon: <img src={chat} alt="message" />, text: "message", href: "/message", active:false},
        {icon: <img src={credit_card} alt="transactions" />, text: "transactions", href: "/transactions", active:false},
    ];
    return (
        <nav className="w-full bg-white flex items-center justify-between px-4 py-2 rounded-[70px]">
            <div className="banner">
                <img src={logo} alt="site banner w-[210.58px] h-12"/>
            </div>
            <ul className="nav-items flex items-center gap-6">
                {navItems.map((item, index) => (
                    <NavItem key={index} icon={item.icon} text={item.text} href={item.href} active={item.active}/>
                ))}
            </ul>
            <div className="accessibility divide-gray-100 flex items-center gap-4">
                <div className="profile flex items-center gap-2">
                    <img src={profile_image} alt="profile" className="w-10 h-10"/>
                    <div className="title">
                        <p className="text-gray-800 text-sm font-bold">Dr. Josse Simmons.</p>
                        <p className="text-gray-400 text-xs capitalize">general practitioner</p>
                    </div>
                </div>
                <div className="settings flex items-center gap-2">
                    <img src={settings} alt="settings" className="w-[`8.94px] h-5"/>
                    <img src={more_vert} alt="more" className="w-6 h-5"/>
                </div>
            </div>
        </nav>
    )
}