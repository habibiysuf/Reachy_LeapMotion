using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Text;
using System;

[System.Serializable]
public class Motor
{
    public string name;
    public GameObject gameObject;
    public float targetPosition;
    public float presentPosition;
}

public class Reachy_head : MonoBehaviour
{

    public Motorr[] motors;
    public static Dictionary<string, Motorr> name2motor;
    private int value;
    public string nilai;
    private int roll;
    private int yaw;

    void Start()
    {
        name2motor = new Dictionary<string, Motorr>();

        for (int i = 0; i < motors.Length; i++)
        {
            Motorr m = motors[i];
            name2motor[m.name] = m;
        }
        nilai = null;
    }
    void Update()
    {
        nilai = SampleUserPolling_JustRead.message;
        string[] data_a = nilai.Split(","[0]);
        value = int.Parse(data_a[0]);
        value = value * 2;
        roll = int.Parse(data_a[1]);
        yaw = int.Parse(data_a[2]);
        //value = int.Parse(nilai);
        //if (value > 45)
        //{
        //    value = 45;
        //}
        
        Motorr m = motors[0];
        JointController joint = m.gameObject.GetComponent<JointController>();
        joint.RotateTo(value);
        m.presentPosition = joint.GetPresentPosition();

        Motorr m2 = motors[1];
        JointController joint2 = m2.gameObject.GetComponent<JointController>();
        joint2.RotateTo(roll);
        m2.presentPosition = joint2.GetPresentPosition();

        Motorr m3 = motors[2];
        JointController joint3 = m3.gameObject.GetComponent<JointController>();
        joint3.RotateTo(yaw);
        m3.presentPosition = joint3.GetPresentPosition();

    }
}
