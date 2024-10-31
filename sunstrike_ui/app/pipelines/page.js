

import {getPipelines} from "../../api/pipeline";

const statuses = { active: 'text-green-400 bg-green-400/10', Error: 'text-rose-400 bg-rose-400/10' }


function classNames(...classes) {
    return classes.filter(Boolean).join(' ')
}

export default async function Pipelines() {
    const pipelines = await getPipelines()

    return (
        <div className="bg-gray-700 py-10 min-h-full">

            <h2 className="px-4 text-base font-semibold leading-7 text-white sm:px-6 lg:px-8">Latest activity</h2>
            <table className="mt-6 whitespace-nowrap text-left w-full">
                <colgroup>
                    <col className=""/>
                    <col className=""/>
                    <col className=""/>
                    <col className=""/>
                    <col className=""/>
                </colgroup>
                <thead className="border-b border-white/10 text-sm leading-6 text-white">
                <tr>
                    <th scope="col" className="py-2 pl-4 pr-8 font-semibold sm:pl-6 lg:pl-8">
                        Pipeline
                    </th>
                    <th scope="col" className="hidden py-2 pl-0 pr-8 font-semibold sm:table-cell">
                        Id
                    </th>
                    <th scope="col" className="py-2 pl-0 pr-4 text-right font-semibold sm:pr-8 sm:text-left lg:pr-20">
                        Status
                    </th>
                </tr>
                </thead>
                <tbody className="divide-y divide-white/5">
                {pipelines.map((item) => (
                    <tr key={item.id}>
                        <td className="py-4 pl-4 pr-8 sm:pl-6 lg:pl-8">
                            <div className="flex items-center gap-x-4">
                                {/*<img src={item.user.imageUrl} alt="" className="h-8 w-8 rounded-full bg-gray-800"/>*/}
                                <div
                                    className="truncate text-sm font-medium leading-6 text-white">{item.name}</div>
                            </div>
                        </td>
                        <td className="hidden py-4 pl-0 pr-4 sm:table-cell sm:pr-8">
                            <div className="flex gap-x-3">
                                <div className="font-mono text-sm leading-6 text-gray-400">{item.id}</div>
                            </div>
                        </td>
                        <td className="py-4 pl-0 pr-4 text-sm leading-6 sm:pr-8 lg:pr-20">
                            <div className="flex items-center justify-end gap-x-2 sm:justify-start">
                                <time className="text-gray-400 sm:hidden" dateTime={item.status}>
                                    {item.date}
                                </time>
                                <div className={classNames(statuses[item.status], 'flex-none rounded-full p-1')}>
                                    <div className="h-1.5 w-1.5 rounded-full bg-current"/>
                                </div>
                                <div className="hidden text-white sm:block">{item.status}</div>
                            </div>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    )
}
