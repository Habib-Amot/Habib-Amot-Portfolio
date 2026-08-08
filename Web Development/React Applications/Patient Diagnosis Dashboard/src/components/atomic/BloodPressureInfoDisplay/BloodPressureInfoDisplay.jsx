import { LuChevronUp, LuChevronDown } from "react-icons/lu"

export default function SystolicBloodPressureInfoDisplay({readings}){
    return (
        <div className="flex flex-col gap-4 pb-5">
            <div className="flex items-center gap-3">
                <span className="w-3 h-3 rounded-full bg-[#E66FD2]"></span>
                <p className="text-sm font-bold">Systolic</p>
            </div>
            <b className="text-[22px] font-extrabold">{readings.value}</b>
            <p className="text-[10px] flex gap-1 items-center">{readings.level.toLowerCase() == "lower than average" ? <LuChevronDown/> : readings.level.toLowerCase() == "higher than average" ? <LuChevronUp/> : null} {readings.level}</p>
        </div>
    )
}


function DiastolicBloodPressureInfoDisplay({readings}){
    return (
        <div className="flex flex-col gap-4 pt-5">
            <div className="flex items-center gap-3">
                <span className="w-3 h-3 rounded-full bg-[#8C6FE6]"></span>
                <p>Diastolic</p>
            </div>
            <b className="text-[22px] font-extrabold">{readings.value}</b>
            <p className="text-[10px] flex gap-1 items-center">{readings.level.toLowerCase() == "lower than average" ? <LuChevronDown/> : readings.level.toLowerCase() == "higher than average" ? <LuChevronUp/> : null} {readings.level}</p>
        </div>
    )
}

export {DiastolicBloodPressureInfoDisplay}