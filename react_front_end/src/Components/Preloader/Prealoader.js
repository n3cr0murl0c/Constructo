import React, { useEffect } from "react";
import './preloader.css';
import { preLoaderAnim } from "../../animations";


const Preloader = () => {

    useEffect(()=>{
        preLoaderAnim()
    },[]);



    return (
        <div className="preloader">
            <div className="flex">
                <div className="row">
                    <div className="texts-container1">
                        <span>Constructo</span>
                    </div>
                </div>

                <div className="row">
                    <div className="texts-container">
                        <span>Diseñamos</span>
                        <span>con</span>
                        <span>Pasión</span>
                    </div>

                </div>
            </div>
            
            
        </div>
    )
}

export default Preloader;